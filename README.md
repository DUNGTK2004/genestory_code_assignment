# 🗂️ FastAPI Task Manager

## 🧩 Giới thiệu

Dự án này là một **Task Manager API** được xây dựng bằng **[FastAPI](https://fastapi.tiangolo.com/)** — một web framework hiện đại, nhanh và dễ dùng cho Python.  
Ứng dụng sử dụng **SQLite** làm cơ sở dữ liệu nhẹ để lưu trữ danh sách các công việc (“tasks”).  

---

## 🎯 Mục tiêu dự án

Mục đích của bài tập này là giúp bạn thực hành cách xây dựng **REST API** với FastAPI kết hợp cùng **SQLAlchemy ORM** và **Pydantic**, thông qua việc phát triển một ứng dụng quản lý công việc đơn giản.  

### 🧠 Sau khi hoàn thành, bạn sẽ nắm được:
- Cách tạo RESTful API bằng FastAPI.  
- Cách định nghĩa **SQLAlchemy ORM models** và kết nối với cơ sở dữ liệu SQLite.  
- Sử dụng **Pydantic schemas** cho việc xác thực request và định dạng response.  
- Triển khai đầy đủ các thao tác **CRUD (Create, Read, Update, Delete)** qua API endpoints.  
- Hiểu được cấu trúc cơ bản của một dự án FastAPI dạng module.  

---

# 🚀 Hướng dẫn chạy dự án FastAPI

## 1️⃣ Tạo môi trường ảo

Tạo môi trường ảo tên **myenv**:

```bash
python -m venv myenv
```

Kích hoạt môi trường ảo:

- **Windows:**
  ```bash
  myenv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source myenv/bin/activate
  ```

---

## 2️⃣ Cài đặt các phụ thuộc

Sau khi kích hoạt môi trường ảo, cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Chạy ứng dụng FastAPI

Khởi động server bằng **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

Sau khi chạy, mở trình duyệt và truy cập địa chỉ:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 4️⃣ Xem tài liệu API

FastAPI tự động sinh ra tài liệu API tại:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

✅ **Hoàn tất!**  
Giờ bạn có thể bắt đầu phát triển, kiểm thử và mở rộng API Task Manager của mình. 🚀
