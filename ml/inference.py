import pickle
import mlflow
from sqlalchemy.orm import Session
from models import PredictionLog
from datetime import datetime

(model, vectorizer) = pickle.load(open("ml/model.pkl", "rb"))
mlflow.set_tracking_uri("file:./mlflow")

# Chọn experiment name
experiment_name = "inference_experiment"

# Tạo experiment nếu chưa tồn tại
if mlflow.get_experiment_by_name(experiment_name) is None:
    mlflow.create_experiment(experiment_name)

mlflow.set_experiment(experiment_name)

def predict_priority(db: Session, text: str, task_id: int | None = None) -> str:
    with mlflow.start_run(run_name="inference") as run:
        X = vectorizer.transform([text])
        pred = model.predict(X)[0]

        log = PredictionLog(
            task_id=task_id,
            input_text=text,
            predicted_priority=pred,
            mlflow_run_id=run.info.run_id,
            timestamp=datetime.utcnow(),
        )

        db.add(log)
        db.commit()
    
        mlflow.log_param("task_id", task_id)
        mlflow.log_param("input_length", len(text))
        mlflow.log_metric("dummy_metric", 1)

    return pred
