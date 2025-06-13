# 📝 Django Content Management App

A user-friendly content management system built with **Django** and **Bootstrap 5**. It allows anyone to browse and read content freely, while registered users can manage content, post topics, comment, and update their profiles.

---

## 🌐 Live Demo

👉 [https://trishna15.pythonanywhere.com/](https://trishna15.pythonanywhere.com/)

> ⚠️ *Note: It may take a few seconds to load if it's hosted on PythonAnywhere's free tier.*

---

## 📌 Features

- 📖 Public access to browse and read content
- 🧑‍💻 User registration and login for content creators
- 🗂 Create, update, and delete:
  - Topics
  - Content under topics
- 💬 Add comments to content
- 👤 Automatic profile creation upon registration
- 🖼 Update profile info and upload profile picture
- 🔐 Password reset and change features
- 🎨 Responsive frontend built with **Bootstrap 5**
- ⚙️ Admin dashboard for superusers via Django admin

---

## 🛠 Tech Stack

- **Python 3.x**
- **Django (latest stable)**
- **SQLite** (default DB)
- **Bootstrap 5** (via CDN)
- **Django Templates**
- **Django Auth System**
- **Deployed on PythonAnywhere**

---


---

## 🚀 Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/trish0912/Django_Content_Mgmnt_App.git
cd Django_Content_Mgmnt_App
```
Create a virtual environment and install dependencies
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Apply migrations and create superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
Run the development server
```
python manage.py runserver
App: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/
```
🔓 Visitors (no login)
Can browse all topics and content

No account needed

🔐 Registered Users
Can create, edit, delete topics and content

Can comment on content

Have a personal profile (with picture)

Can update profile info and reset password

🎨 Frontend Design
Fully responsive using Bootstrap 5

Styled navigation, buttons, forms, and cards

Easy to customize via templates and static CSS

🚀 Deployment
This project is deployed on PythonAnywhere:

🔗 Live URL: https://trishna15.pythonanywhere.com

Hosting includes:

GitHub integration

WSGI config

Media/static path setup

collectstatic, migrate, createsuperuser

PythonAnywhere deployment guide:
https://help.pythonanywhere.com/pages/DeployingDjango/


🙋‍♀️ Author
Trishna Roy

GitHub: @trish0912

LinkedIn: www.linkedin.com/in/trishna-r-06026914a

