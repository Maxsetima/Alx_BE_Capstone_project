# E-commerce Capstone Project
# 🌽 E-Commerce API for Farmers, Consumers, and Logistics Companies
## Project Overview

This project is an E-commerce platform that connects rural farmers to urban markets. The project focuses on livestock rearing and vegetable farming, enhancing farmers' access to urban markets while streamlining logistics.
This is a Django REST Framework-powered API that enables farmers to list and sell products, consumers to order and review products, and logistics companies to handle delivery. Built for quick, secure, and scalable transactions across the agricultural supply chain.

---

## 🚀 Features

- 🔐 Token-based authentication (DRF authtoken)
- 🧑‍🌾 Farmers: Add, update, and manage products
- 🛒 Consumers: Browse products, place orders, make payments, review purchases
- 🚚 Logistics Companies: Track, update, and confirm deliveries
- 📦 Order management
- 💳 Payment integration (simulated or real)
- ⭐ Product reviews
- 🌍 Scalable architecture (apps: `accounts`, `products`, `orders`, `payments`, `logistics`, `reviews`)

---

## 📂 Project Structure


## Features

- **User Authentication:** Registration, login, and profile management for Farmers, Consumers, and Logistics Companies.
- **Product Management:** Farmers can list, create, update, and delete products (livestock and vegetables).
- **Order Management:** Consumers can place orders and track order status.
- **Logistics Integration:** Seamless integration with logistics companies for product transportation.
- **Payment Integration:** Secure payment processing using mobile payment solutions (e.g., M-Pesa).
- **Review System:** Consumers can rate and review products and sellers.
- **Advanced Features:** Tagging, search functionality, filtering, and pagination for improved user experience.

## Directory Structure


## How to Run the Project

1. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows; use `source venv/bin/activate` on macOS/Linux


## Project Overview


## Features Implemented This Week
- **Cart Functionality:** Users can add, update, and remove items from their cart.
- **Order Processing:** Users can place orders and view order details.
- **User Authentication Improvements:** Implemented password reset functionality (and plans for email verification).
- **API Testing:** Endpoints were tested using Postman and curl.
- **Additional Refinements:** Improved error handling and data validation across endpoints.

## How to Run
1. **Set up a virtual environment:**

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the repository

```bash
git clone https://github.com/your-username/ecommerce_project.git
cd ecommerce_project

## 2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows; use venv/bin/activate on macOS/Linux AUTH_USER_MODEL = 'api.CustomUser'
   source venv/bin/activate  # Windows: venv\Scripts\activate

## 3. Install dependencies

## pip install -r requirements.txt

 ## 4. Set up MySQL database
 Ensure MySQL is installed and running.

 Create a database and user:

 CREATE DATABASE my_ecommerce_db;
CREATE USER 'my_ecommerce_user'@'localhost' IDENTIFIED BY 'SangSetim3502';
GRANT ALL PRIVILEGES ON my_ecommerce_db.* TO 'my_ecommerce_user'@'localhost';

## Configure DATABASES in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_ecommerce_db',  # The name of your database
        'USER': 'my_ecommerce_user',  # The MySQL user you've just created
        'PASSWORD': 'SangSetim3502',  # The password for the MySQL user
        'HOST': 'localhost',  # Host for the database (localhost for local setup)
        'PORT': '3306',  # Default MySQL port
    }
}

## 5. Run migrations

python manage.py makemigrations
python manage.py migrate

##  6. Create superuser
python manage.py createsuperuser

Testing the API
Obtain Auth Token
http:
POST /api-token-auth/
{
  "username": "your_username",
  "password": "your_password"
}


## Returns:
json
{ "token": "your_auth_token" }

## 🛒 Add a Product
http;

POST /api/products/
Authorization: Token your_auth_token
Content-Type: application/json

{
  "name": "Organic Maize",
  "description": "Fresh from the farm",
  "price": "1200.00",
  "stock": 100
}

## 📦 Place Order
http;
POST /api/orders/
Authorization: Token your_auth_token

{
  "product": 1,
  "quantity": 2
}

## 💳 Make Payment
http;

## POST /api/payments/
Authorization: Token your_auth_token

{
  "order_id": 1,
  "payment_method": "mpesa"
}

## ⭐ Leave a Review
POST /api/reviews/
Authorization: Token your_auth_token

{
  "product": 1,
  "rating": 5,
  "comment": "Great product!"
}
## 🚚 Logistics Update
PATCH /api/logistics/1/
Authorization: Token logistics_user_token

{
  "status": "Delivered"
}

## 📌 API Authentication
All protected endpoints require this header:

Authorization: Token <your_token_here>

## 💻 Run the Development Server

python manage.py runserver

Navigate to:
http://127.0.0.1:8000/api/products/

---

## ✅ PART 2: 🧾 GitHub Commit & Push

### 🔁 1. Stage your changes

```bash
git add .

## 2. Commit the changes
git commit -m "Add full API functionality for products, orders, payments, reviews, logistics"

## 3. Push to GitHub
Make sure your GitHub repo is created and the remote is set:
git remote add origin https://github.com/your-username/ecommerce_project.git

Then:
git push -u origin main

If you've already connected your remote, just run:
git push



SECRET_KEY = 'django-insecure-ou3@*hzg_s*8ikym*yp!#ey5p9n_gehx)*^%^xaawl%(s(l_y@'
8fadbce8d549c0fe3c9b0a4501c49b3487ead1a7	Sang
21a6adcdf6240ccce34cf51fda4d53f9ac346ba6	Customuser