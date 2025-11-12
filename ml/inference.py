import pickle
import mlflow
from sqlalchemy.orm import Session
from models import PredictionLog, Task
from datetime import datetime
import os

# --- Danh sách các model có sẵn ---
MODEL_FILES = {
    "LogisticRegression": "ml/LogisticRegression_model.pkl",
    "MultinomialNB": "ml/MultinomialNB_model.pkl",
    "ComplementNB": "ml/ComplementNB_model.pkl"
}

mlflow.set_tracking_uri("file:./mlflow")

# Chọn experiment name
experiment_name = "inference_experiment"

# Tạo experiment nếu chưa tồn tại
if mlflow.get_experiment_by_name(experiment_name) is None:
    mlflow.create_experiment(experiment_name)

mlflow.set_experiment(experiment_name)


def predict_priority(
    db: Session,
    title: str,
    description: str,
    task_id: int | None = None,
    auto_assign: bool = True,
    model_name: str = "LogisticRegression"  # chọn model để dùng
) -> str:
    """
    Dự đoán priority của một task dựa trên tiêu đề và mô tả của task đó.
    
    Args:
        db (Session): Session của database
        title (str): Tiêu đề của task
        description (str): Mô tả của task
        task_id (int | None): ID của task được dự đoán
        auto_assign (bool): Nếu True, tạo task mới với priority dự đoán
        model_name (str): Tên model để sử dụng ('logreg', 'naivebayes', 'randomforest')
        
    Returns:
        str: Priority dự đoán của task
    """
    # --- Load model & vectorizer tương ứng ---
    if model_name not in MODEL_FILES:
        raise ValueError(f"Model '{model_name}' không tồn tại. Chọn trong {list(MODEL_FILES.keys())}")

    model_path = MODEL_FILES[model_name]
    with open(model_path, "rb") as f:
        model, vectorizer = pickle.load(f)

    text = title + " " + (description or "")
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]

    # --- Lưu log vào database ---
    log_entry = PredictionLog(
        task_id=task_id,
        title=title,
        description=description,
        predicted_priority=pred,
        mlflow_run_id=None,  # sẽ cập nhật sau khi log MLflow
        timestamp=datetime.utcnow()
    )
    db.add(log_entry)

    # --- Tạo task mới nếu auto_assign=True ---
    if auto_assign:
        new_task = Task(
            title=title,
            description=description,
            priority=pred,
            is_done=False
        )
        db.add(new_task)

    # db.refresh(log_entry)

    # --- Log vào MLflow ---
    run_name = f"{model_name}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
    with mlflow.start_run(run_name=run_name) as run:
        mlflow.log_param("task_id", task_id)
        mlflow.log_param("input_length", len(text))
        mlflow.log_param("title", title)
        mlflow.log_param("description", description)
        mlflow.log_param("predicted_priority", pred)
        mlflow.log_param("model_name", model_name)
        # Cập nhật MLflow run id vào PredictionLog
        log_entry.mlflow_run_id = run.info.run_id
        db.commit()

    return pred
