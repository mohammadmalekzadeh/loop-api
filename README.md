![Loop](https://www.lloop.ir/icon/favicon.png)

The **LOOP API (Back-End)** provides backend services for the LOOP platform.
Built with **FastAPI** and **SQLAlchemy**, it handles authentication, data persistence, and business logic for reducing food waste.

---

## 📌 Technologies Used

- **Language:** Python 3.13
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgresSQL
- **Migrations:** Alembic
- **Auth:** JWT

---

## 📂 Project Structure

```bash
loop-api/
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
│
├─── .github/workflows
│       liara.yaml
├─── alembic/
│       env.py
│       script.py.mako
│       versions/
├─── app/
│   ├── api/v1/endpoints/
│   ├── core/
│   ├── db/
│   ├── deps/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── utils/
└─── tests/

```

---

## 🔄 CI/CD

This project includes a **GitHub Actions** workflow for:  
- Running tests  
- Building the app  
- Deploying to hosting providers (e.g., Render, Liara or custom servers)  

Workflow configuration is stored in `.github/workflows/`.

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## 📬 Contact
Maintained by **Mohammad Malekzadeh**.  
Questions? Issues? Feature requests? Just open an issue or reach out via GitHub!