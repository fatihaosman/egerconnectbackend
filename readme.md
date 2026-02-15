# 🚀 EgerConnect – Campus Information & Student Support System

## 📌 Overview

**EgerConnect** is a backend-powered campus information management system built using **Django** and **Django REST Framework (DRF)**.

The system is designed to:

- Manage campus notices
- Provide secure user authentication
- Support structured content management
- Serve as a foundation for events, lost & found, and scholarship systems

This project is being developed as part of the **ALX Backend Capstone Project (Part 3 – Start Building)**.

---

## 🛠 Tech Stack

- Python 3.12
- Django
- Django REST Framework
- SQLite (Development Database)
- Postman (API Testing)

---

## ✅ Features Implemented

### 🔐 1. Custom Authentication System

- Implemented a **custom User model**
- Authentication using **email instead of username**
- Secure password hashing using Django's `create_user()` method
- Superuser (admin) creation supported

#### Authentication Endpoints:

- `POST /api/auth/register/`
- `POST /api/auth/login/`

Authentication has been tested successfully using Postman.

---

### 📢 2. Notice Management System

Implemented a Notice API with the following fields:

- `title` – Short notice title
- `image` – Optional image upload
- `created_at` – Automatically records posting date

#### Notice Endpoints:

- `GET /api/posts/notices/`
  - Public access
  - Returns notices ordered by latest first

- `POST /api/posts/notices/`
  - Admin-only access
  - Creates a new notice

#### Permissions:

- Anyone can view notices
- Only admin users (`is_staff=True`) can create, update, or delete notices

---

### 🖼 Media Upload Configuration

- Configured `MEDIA_URL` and `MEDIA_ROOT`
- Enabled image uploads using Django’s `ImageField`
- Images stored in `/media/notices/`

---

## 📂 Project Structure

