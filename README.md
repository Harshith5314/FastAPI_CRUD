# Full Stack FastAPI CRUD Application 🚀

A comprehensive full-stack web application demonstrating **Create, Read, Update, and Delete (CRUD)** operations.

This project connects a high-performance **FastAPI backend** (with PostgreSQL/SQLAlchemy) to a live cloud environment on Render, serving as a practical reference for modern web development architecture and deployment.

## 🌐 Live Demo & Documentation
The project is fully deployed and active. You can interact with the API directly via the live links below:

* **🟢 Live API Base URL:** [https://fastapi-crud-project-mylh.onrender.com/](https://fastapi-crud-project-mylh.onrender.com/)
* **📄 Interactive Docs (Swagger UI):** [https://fastapi-crud-project-mylh.onrender.com/docs](https://fastapi-crud-project-mylh.onrender.com/docs)
* **📚 Alternative Docs (ReDoc):** [https://fastapi-crud-project-mylh.onrender.com/redoc](https://fastapi-crud-project-mylh.onrender.com/redoc)

---

## 📚 Project Architecture & Concepts

This project is structured to separate concerns, making it scalable and easy to maintain. Here is how the key files work together:

### 1. The Core Structure
* **`main.py`**: The **API Layer**. Initializes the `FastAPI` app, handles routing (`@app.get`, `@app.post`), and manages the database session lifecycle using **Dependency Injection** (`get_db`). It also includes **CORS** configuration to allow frontend communication.
* **`database.py`**: The **Connection Layer**. It intelligently switches between the live Render database (`DATABASE_URL`) and a local PostgreSQL instance for development. It creates the SQLAlchemy `engine` and session.
* **`database_models.py`**: The **Database Layer**. Contains **SQLAlchemy Models** that define the structure of your SQL tables (e.g., `Product` table with columns `id`, `name`, `price`, `quantity`).
* **`models.py`**: The **Validation Layer**. Uses **Pydantic Models** to validate incoming request data (e.g., ensuring `price` is a float) before it reaches the database logic.
* **`requirements.txt`**: Lists all the necessary Python libraries (`fastapi`, `uvicorn`, `sqlalchemy`, etc.) required for the cloud deployment.

---

## 🛠️ Tech Stack & Libraries

| Component | Library | Role |
| :--- | :--- | :--- |
| **Framework** | `fastapi` | The main web framework handling routing and high-performance requests. |
| **Server** | `uvicorn` | The ASGI server that listens to the network and runs the Python code. |
| **ORM** | `sqlalchemy` | Translates Python classes into SQL queries for the database. |
| **Driver** | `psycopg2` | The adapter that allows Python to talk to PostgreSQL. |
| **Validation** | `pydantic` | Ensures input data is correct (the "Guard at the door"). |
| **Deployment** | `Render` | Cloud platform hosting the API and PostgreSQL database. |

---

## ⚡ Getting Started (Local Development)

Follow these steps to run the application on your local machine for development or testing.

### Prerequisites
* **Python 3.9+**
* **PostgreSQL** (running locally)

### Phase 1: Setup & Installation

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
    pip install -r requirements.txt
    ```

4.  **Configure Local Database**
    * Ensure your local PostgreSQL server is running.
    * Open `database.py`.
    * The script automatically uses the fallback URL if no cloud environment is detected:
      ```python
      # Default local connection
      "postgresql://postgres:1323@localhost:5432/harshith"
      ```
    * *Note: Update the username/password in `database.py` if yours differs.*

5.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```
    * The Backend is now running at `http://127.0.0.1:8000`.
    * Interactive Docs are available at `http://127.0.0.1:8000/docs`.

---

## 🔌 API Endpoints Reference

| Method | Endpoint | Functionality |
| :--- | :--- | :--- |
| **GET** | `/` | Health check / Welcome message. |
| **GET** | `/products` | Fetch all products from the database. |
| **GET** | `/products/{id}/` | Fetch a single product by its ID. |
| **POST** | `/products` | Create a new product (Requires JSON body). |
| **PUT** | `/products` | Update an existing product (Requires `id` query param). |
| **DELETE**| `/products` | Remove a product from the database (Requires `id` query param). |

---

## ☁️ Deployment Guide (Render)

This project is configured for seamless deployment on [Render.com](https://render.com).

1.  **Create Database:**
    * Create a new **PostgreSQL** service on Render.
    * Copy the `Internal Database URL`.

2.  **Create Web Service:**
    * Connect your GitHub repo.
    * **Build Command:** `pip install -r requirements.txt`
    * **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`

3.  **Environment Variables:**
    * Add a variable named `DATABASE_URL`.
    * Paste the internal database URL from Step 1.

---

## 🤝 Contributing
Feel free to fork this project and submit Pull Requests to improve the validation, add new features, or enhance the documentation!
