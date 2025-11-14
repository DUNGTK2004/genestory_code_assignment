# FastAPI Task Manager + MLflow (Assignment 2)

Dự án mở rộng Task Manager từ Assignment 1 bằng cách tích hợp mô hình Machine Learning để dự đoán mức độ ưu tiên của task ("Low", "Medium", "High") và sử dụng MLflow để theo dõi toàn bộ quá trình huấn luyện – inference.

## 🚀 Features

* CRUD Task API bằng FastAPI
* Dự đoán priority từ `title + description`
* Mô hình ML (TF-IDF + Logistic Regression hoặc Naive Bayes)
* Tracking đầy đủ bằng MLflow:
  * parameters
  * metrics
  * artifacts
  * run ID
* Ghi log dự đoán vào SQLite (PredictionLog)
* Lưu mô hình tại `ml/model.pkl`

## 📦 Project Structure
```
fastapi-task-manager/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
│
├── ml/
│   ├── train_model.py
│   ├── inference.py
│   ├── model.pkl
│
├── mlflow/
│   └── mlruns/
│
├── tasks.db
└── requirements.txt
```

## ⚙️ Installation

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Start MLflow UI
```bash
mlflow ui
```

→ http://127.0.0.1:5000

## 🧠 Training the Model

Chạy script huấn luyện:
```bash
python ml/train_model.py
```

Script sẽ:
* load dữ liệu từ SQLite
* TF-IDF vector hóa
* train model
* log parameters/metrics lên MLflow
* lưu mô hình vào `ml/model.pkl`

## 🔮 Prediction API

### Endpoint
```
POST /predict-priority/
```

### Request
```json
{
  "title": "Fix API error",
  "description": "Server returns 500 frequently"
}
```

### Response
```json
{
  "predicted_priority": "High"
}
```

Khi dự đoán:
* Model được load từ `ml/model.pkl`
* Lưu log vào bảng `PredictionLog`
* Log inference lên MLflow

## ▶️ Running the Application

### Start FastAPI
```bash
uvicorn main:app --reload
```

### API Docs

http://127.0.0.1:8000/docs

## 📝 Notes

* Dataset gồm các task được lưu trong SQLite.
* Chỉ train trên các task chưa hoàn thành (`is_done = False`).
* Text input = `title + description`.
* Mỗi lần train tạo 1 MLflow run mới → xem lịch sử trong UI.
