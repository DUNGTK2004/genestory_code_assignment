import sys, os
import random
import pickle, mlflow, mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.metrics import accuracy_score, f1_score
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

# Đảm bảo có thể import các module từ thư mục cha
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models import Task

# Set seed cho việc tái lập kết quả
SEED = 42
random.seed(SEED)

# Thiết lập MLflow
mlflow.set_tracking_uri("file:../mlflow")
mlflow.set_experiment("TaskPriorityPrediction")

# Kết nối database
db = SessionLocal()

# Load dữ liệu
tasks = db.query(Task).filter(and_(Task.is_done == False, Task.priority != None)).all()

texts = [t.title + " " + (t.description or "") for t in tasks]
labels = [t.priority for t in tasks]

print(labels)
# Chia dữ liệu 
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=SEED)

# Thử nghiệm với nhiều mô hình
models_to_run = [
    ("LogisticRegression", LogisticRegression(max_iter=200, random_state=SEED)),
    ("MultinomialNB", MultinomialNB(random_state=SEED)),
    ("ComplementNB", ComplementNB(random_state=SEED))
]

for model_name, model in models_to_run:
    # Tất cả các log metrics, params, artifacts trong khối này sẽ thuộc cùng một experiment run
    with mlflow.start_run(run_name=f"{model_name}_tfidf"): 
        mlflow.log_param("model_type", model_name)
        mlflow.log_param("vectorizer", "TF-IDF")
        mlflow.log_param("test_split", 0.2)
        mlflow.log_param("random_seed", SEED)

        # transform data cho huấn luyện
        vectorizer = TfidfVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)

        # Huấn luyện mô hình
        model.fit(X_train_vec, y_train)

        # Dự đoán và đánh giá
        preds = model.predict(X_test_vec)
        print(f"Predictions: {preds}")
        print(f"Evaluating model... {y_test} vs {preds}")
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average='weighted')

        # Log metrics
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        # Lưu mô hình và vectorizer
        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(script_dir, f"{model_name}_model.pkl")
        pickle.dump((model, vectorizer), open(model_path, "wb"))

        # Log artifact gồm model và vectorizer
        mlflow.log_artifact(model_path)

    print(f"{model_name} trained with Accuracy: {acc}, F1-Score: {f1}")

db.close()