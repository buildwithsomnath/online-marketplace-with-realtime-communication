# 🛒 Online Marketplace with Real-Time Communication

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

> A secure, responsive, and user-friendly e-commerce platform built with Django, enabling buyers and sellers to connect, transact, and communicate seamlessly.

🔗 **Live Project**: [GitHub Repository](https://github.com/dassomnath99/Online-Marketplace)  
👤 **Author**: [Somnath Das](https://github.com/dassomnath99)

---

## 📌 Problem Statement

Traditional local marketplaces often lack digital infrastructure, making it difficult for small-scale sellers to reach a wider audience and for buyers to discover trusted vendors. Existing platforms may be complex, expensive, or not tailored for local commerce.

**Key challenges addressed:**
- Fragmented buyer-seller communication
- Absence of a unified, secure transaction environment
- Lack of real-time product discovery and filtering
- Poor mobile experience for users in emerging markets

This project aims to bridge that gap by providing a **lightweight, scalable, and intuitive online marketplace** that empowers local entrepreneurs and offers buyers a seamless shopping experience.

---

## 💡 Solution Approach

The **Online Marketplace** is a full-stack web application designed with a focus on usability, performance, and security. Built using **Python and Django** on the backend and enhanced with **TailwindCSS** for a modern, responsive frontend, it offers end-to-end e-commerce functionality.

### ✨ Core Features

- **User Authentication & Profiles**: Secure sign-up/login with role-based access (buyer/seller).
- **Product Management**: Sellers can list, edit, and manage their products with images and categories.
- **Advanced Search & Filtering**: Buyers can search products by name, category, price range, and seller.
- **Real-Time Messaging**: Integrated chat system for direct buyer-seller communication.
- **Order Tracking**: Users can view order history and current status.
- **Responsive UI**: Fully mobile-optimized using TailwindCSS and modern HTML5/CSS3 practices.
- **Secure Architecture**: Password hashing, CSRF protection, and input validation built-in via Django.

### 🧠 Technical Design

- **Backend**: Django (MVT architecture) with Django REST principles for internal logic.
- **Frontend**: HTML5, CSS3, JavaScript (basic), and TailwindCSS for utility-first styling.
- **Database**: SQLite (development), easily swappable to MySQL for production.
- **State Management**: Server-rendered templates with Django context passing (no heavy frontend framework for simplicity and speed).
- **Security**: Django’s built-in auth system, secure session handling, and form validation.

> 💡 *Part of Somnath Das’s portfolio as a Full-Stack Developer and recent B.Tech graduate (IT, University of Kalyani, 2025).*

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)
- Git

### 📥 Clone the Repository

```bash
git clone https://github.com/dassomnath99/Online-Marketplace.git
cd Online-Marketplace
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Install the requirement libarires
pip install -r requirements.txt
pip install django pillow

# run makemigrations and migrate them
python manage.py makemigrations
python manage.py migrate

#create a super user for database
python manage.py createsuperuser

#Run the server
python manage.py runserver
