# LOOP API (Backend)

The **LOOP API** provides backend services for the LOOP platform. Built with **FastAPI** and **SQLAlchemy**, it handles authentication, data persistence, and business logic for reducing food waste.

---

## 📌 Technologies Used

* **Language:** Python
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Database:** PostgreSQL
* **Migrations:** Alembic

---

## 📂 Structure

```
backend/
│   alembic.ini
│   main.py
│   requirements.txt
│
├── app/v1/
│   ├── core/        # Config and security
│   ├── database/    # DB base, session, init
│   ├── deps/        # Dependencies
│   ├── models/      # ORM models
│   ├── routers/     # API endpoints
│   ├── schemas/     # Pydantic schemas
│   ├── services/    # Business logic
│   └── utils/       # Utilities
│
└── tests/           # Unit tests
```

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## 📬 Contact
Maintained by **Mohammad Malekzadeh**.  
Questions? Issues? Feature requests? Just open an issue or reach out via GitHub!