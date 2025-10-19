# Profile_API

A simple Django REST API for managing user profiles.  
This project is designed to demonstrate CRUD operations, authentication, and API best practices using Django and Django REST Framework (DRF).

---

## 🚀 Features
- User registration and authentication
- Create, Read, Update, Delete (CRUD) user profiles
- Token-based authentication
- Django REST Framework integration
- Environment variable management with `.env`

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Django 5+**
- **Django REST Framework**
- **SQLite3 / PostgreSQL (configurable)**
- **Virtual Environment** (venv)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/maj-alero/Profile_API.git
cd Profile_API
```
### 2️⃣ Create and Activate a Virtual Environment
## Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## Mac OS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a .env File
```bash
CAT_FACT_API=https://catfact.ninja/fact
API_TIMEOUT=your_timeout_figure
```
### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```
### Author
Amaju Ogbe (maj-alero)
[GitHub Profile](https://github.com/maj-alero/)