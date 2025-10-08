![Loop](https://www.lloop.ir/icon/favicon.png)

The **Loop API** is a modern backend built with **FastAPI**, designed for managing users, products, vendors, and requests.
It uses **SQLAlchemy ORM** for database interaction, **Alembic** for migrations, **JWT** for authentication, and **Docker** for easy deployment.

---

## ✨ Features

- ⚡ Fast and modular architecture with **FastAPI**
- 🔐 **JWT** authentication
- 🗄️ **SQLAlchemy** + **Alembic** for database management
- 🧱 Layered structure (API / Models / Schemas / Core)
- 🐳 **Docker** & **Docker Compose** for containerized deployment
- 🔁 Optional **Redis** integration
- 🌐 Versioned API (v1)

---

## 📌 Technologies Used

- **Language:** Python 3.11
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgresSQL
- **Migrations:** Alembic
- **Auth:** JWT

---

## 📂 Project Structure

```bash
loop-api/
│
├── app/                     # Main application source
│   ├── api/v1/endpoints/    # Routers & API endpoints
│   │   ├── auth/            # Login, signup, OTP verification
│   │   ├── product/         # Product management
│   │   ├── vendors/         # Vendor logic & avatar upload
│   │   ├── profile/         # Dashboard & profile routes
│   │   └── request/         # Request management
│   │
│   ├── core/                # Configuration, Redis client, security
│   ├── db/                  # Database setup (Base, Session, Init)
│   ├── deps/                # Dependency injections
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Service layer logic
│   └── utils/               # Utility functions (OTP, SMS, etc.)
│
├── alembic/                 # Alembic migrations
│   ├── versions/            # Migration files
│   └── env.py
│
├── tests/                   # Unit tests
│
├── .env.example             # Example environment configuration
├── docker-compose.yml       # Docker compose setup
├── Dockerfile               # Docker build instructions
├── requirements.txt         # Python dependencies
├── main.py                  # FastAPI entry point
├── README.Docker.md         # Docker usage guide
├── liara.json               # Liara deployment configuration
└── LICENSE                  # License file
```

---

## 🧩 Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mohammadmalekzadeh/loop-api.git
cd loop-api
```

### 2️⃣ Create your environment file
```bash
cp .env.example .env
```
*Then edit `.env` with your own values (like `DATABASE_URL`, `SECRET_KEY`, etc.).*

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the development server or 🐳 Run with Docker
```bash
uvicorn main:app --reload
```
OR
```bash
docker-compose up --build
```
**Now your API is live at:**
- 👉 http://127.0.0.1:8000/docs
---

## 🔁 Database Migration (Alembic)
Generate and apply migrations using:
```bash
alembic revision --autogenerate -m "init tables"
alembic upgrade head
```

---
## 🧱 Docker Deployment Notes

To deploy using Docker:
- Build: `docker-compose build`
- Run: `docker-compose up`
- Stop: `docker-compose down`

*Environment variables (like `DATABASE_URL`) are loaded from `.env`.*

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## 📬 Contact
Maintained by **Mohammad Malekzadeh**.  
Questions? Issues? Feature requests? Just open an issue or reach out via GitHub!
