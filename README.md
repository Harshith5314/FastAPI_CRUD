# Full Stack FastAPI CRUD Application

A comprehensive full-stack web application demonstrating **Create, Read, Update, and Delete (CRUD)** operations.

This project connects a high-performance **FastAPI backend** (with PostgreSQL/SQLAlchemy) to a **React frontend**, serving as a practical reference for modern web development architecture.

---

## 📚 Project Architecture & Concepts

This project is structured to separate concerns, making it scalable and easy to maintain. Here is how the key files work together:

### 1. The Backend Structure (`/`)
* **`database.py`**: The **Connection Layer**. It creates the SQLAlchemy `engine` (connection to the DB) and the `SessionLocal` class (used to create temporary database sessions for requests).
* **`models.py`**: The **Database Layer**. Contains **SQLAlchemy Models** that define the structure of your SQL tables (e.g., `Product` table with columns `id`, `name`, `price`).
* **`schemas.py` / `main.py`**: The **Validation Layer**. Uses **Pydantic Models** to validate incoming data (e.g., ensuring `price` is a number) before it reaches the database.
* **`main.py`**: The **API Layer**. Initializes the `FastAPI` app, handles routing (`@app.get`, `@app.post`), and manages the database session lifecycle using **Dependency Injection** (`get_db`).

### 2. The Frontend Structure (`/frontend`)
* **React App**: A lightweight UI that fetches data from the backend using HTTP requests.
* **CORS**: The backend is configured to allow requests from the frontend (`localhost:3000`) to prevent browser security errors.

---

## 🛠️ Tech Stack & Libraries

| Component | Library | Role |
| :--- | :--- | :--- |
| **Framework** | `fastapi` | The main web framework handling routing and requests. |
| **Server** | `uvicorn` | The ASGI server that listens to the network and runs the Python code. |
| **ORM** | `sqlalchemy` | Translates Python classes into SQL queries for the database. |
| **Driver** | `psycopg2` | The adapter that allows Python to talk to PostgreSQL. |
| **Validation** | `pydantic` | Ensures input data is correct (the "Guard at the door"). |
| **Frontend** | `React.js` | The user interface (located in `frontend/`). |

---

## ⚡ Getting Started

Follow these steps to run the full application (Backend + Frontend) locally.

### Prerequisites
* **Python 3.9+**
* **Node.js & npm** (for the frontend)
* **PostgreSQL** (running locally or via Docker)

### Phase 1: Backend Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Harshith5314/FastAPI_CRUD.git](https://github.com/Harshith5314/FastAPI_CRUD.git)
    cd FastAPI_CRUD
    ```

2.  **Create Virtual Environment**
    ```bash
    python -m venv venv
    
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
    ```

4.  **Configure Database**
    * Open `database.py`.
    * Update the `SQLALCHEMY_DATABASE_URL` with your PostgreSQL credentials:
        ```python
        # Format: postgresql://username:password@localhost/database_name
        SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/telusko"
        ```

5.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```
    * The Backend is now running at `http://127.0.0.1:8000`.
    * Interactive Docs are available at `http://127.0.0.1:8000/docs`.

---

### Phase 2: Frontend Setup

1.  **Navigate to Frontend Directory**
    Open a **new terminal** window (keep the backend running) and go to the frontend folder:
    ```bash
    cd frontend
    ```

2.  **Install Node Dependencies**
    ```bash
    npm install
    ```

3.  **Start the UI**
    ```bash
    npm start
    ```
    * The Frontend will launch in your browser at `http://localhost:3000`.

---

## 🔌 API Endpoints Reference

| Method | Endpoint | Functionality |
| :--- | :--- | :--- |
| **GET** | `/products` | Fetch all products from the database. |
| **GET** | `/product/{id}` | Fetch a single product by its ID. |
| **POST** | `/product` | Create a new product (Requires JSON body). |
| **PUT** | `/product/{id}` | Update an existing product. |
| **DELETE**| `/product/{id}` | Remove a product from the database. |

---

## 🐛 Troubleshooting

* **CORS Error:** If the frontend cannot talk to the backend, ensure `CORSMiddleware` is added in `main.py` and `allow_origins` includes `http://localhost:3000`.
* **Database Connection Error:** Double-check your username/password in `database.py` and ensure the PostgreSQL service is running.
* **Module Not Found:** Ensure your virtual environment is activated (`(venv)`) before running `uvicorn`.

---

## 🤝 Contributing
Feel free to fork this project and submit Pull Requests to improve the validation or add new features like User Authentication!
