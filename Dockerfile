# Base image
FROM python:3.10-slim

# Làm việc trong /app
WORKDIR /app

# Copy file requirements.txt và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# EXPOSE cổng 8000 của FastAPI và cổng 5000 của MLflow
EXPOSE 8000
EXPOSE 5000

# Lệnh chạy song song FastAPI và MLflow khi container khởi động
CMD bash -c "uvicorn main:app --host 0.0.0.0 --port 8000 & \
             mlflow ui --backend-store-uri file:./mlflow \
                       --default-artifact-root ./mlflow \
                       --host 0.0.0.0 --port 5000 && wait"