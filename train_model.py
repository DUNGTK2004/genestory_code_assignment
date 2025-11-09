import pickle, mlflow, mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task
import os

os.makedirs("ml", exist_ok=True)
mlflow.set_tracking_uri("file:mlflow")
mlflow.set_experiment("TaskPriorityPrediction")

db = SessionLocal()
tasks = db.query(Task).filter((Task.is_done == False) or (Task.priority != None)).all()
print("tasks", tasks)
texts = [t.title + " " + (t.description or "") for t in tasks]
labels = [t.priority for t in tasks]
print(texts[:3], labels[:3])
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=200)
with mlflow.start_run(run_name="logreg_tfidf"):
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("vectorizer", "TF-IDF")

    model.fit(X_train_vec, y_train)
    preds = model.predict(X_test_vec)
    print(f"Predictions: {preds}")
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average='weighted')

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    pickle.dump((model, vectorizer), open("ml/model.pkl", "wb"))
    mlflow.log_artifact("ml/model.pkl")

print(f"Model trained with Accuracy: {acc}, F1-Score: {f1}")
                     