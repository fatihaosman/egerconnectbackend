# EgerConnect 🎓

EgerConnect is a campus information and student support management system built with Django and Django REST Framework.

The platform allows students to:
- Register and log in securely
- View campus announcements and updates
- Submit support requests
- Access information about events, scholarships, and lost & found

Admins can:
- Create and manage campus content
- Review and manage student support requests

---

## 🚀 Features

### 🔐 Authentication
- Custom User model (email-based login)
- JWT authentication (SimpleJWT)
- User registration
- Secure login with token generation
- Role-based permissions (Admin vs Student)

---

### 📢 Content Management

#### Notices
- Admin can create, update, delete
- Public users can view

#### Events
- Image upload supported
- Public viewing
- Admin-only management

#### Lost & Found
- Admin posts items
- Students can view

#### Scholarships / Bursaries
- Admin posts opportunities
- Students can view

---

### 📝 Support Request System

Students can:
- Submit support requests
- Select type of need (Accommodation, Food, Medical, etc.)
- Provide explanation and referee details
- View only their own requests

Admins can:
- View all submitted support requests
- Manage and review them

Admin users cannot submit support requests.

---

## 🛠 Tech Stack

- Python 3.12
- Django
- Django REST Framework
- SimpleJWT
- SQLite (development)
- HTML + CSS (basic frontend templates)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/EgerConnect.git
cd EgerConnect

RUN MIGRATIONS
python manage.py makemigrations
python manage.py migrate

RUN SERVER
python manage.py runserver

OPEN IN BROWSER
http://127.0.0.1:8000/


🔑 API Endpoints
Authentication

POST /api/auth/register/

POST /api/auth/token/

POST /api/auth/token/refresh/


🔑 API Endpoints
Authentication

POST /api/auth/register/

POST /api/auth/token/

POST /api/auth/token/refresh/


project structure.
egerconnect/
│
├── accounts/        # Authentication app
├── posts/           # Content & support system
├── media/           # Uploaded images
├── templates/       # HTML templates
├── manage.py
└── db.sqlite3


🔐 Permissions Logic

Public users: Can view content.

Authenticated students:

Can submit support requests.

Can only view their own requests.

Admin users:

Can manage all posts.

Can view all support requests.

Cannot submit support requests.

📌 Current Status

Backend fully functional

JWT authentication working

Image uploads configured

Basic frontend templates implemented

Role-based permissions enforced