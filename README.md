# Django Book Review API

A robust and well-structured Django backend API for managing a book review application. This project is designed to handle book details, user reviews, authentication, recommendations, and more. It leverages Django, Django REST Framework (DRF), and PostgreSQL for creating a fully functional book review system.

## Features

- **User Authentication**: Secure registration, login, and JWT token-based authentication.
- **Book Management**:
  - Add, update, delete, and retrieve books.
  - Search books by title, author, or ISBN.
  - Sorting and filtering options by title, author, average rating, and genre.
- **Reviews**:
  - Add, edit, delete reviews for books.
  - View all reviews for a specific book.
  - Calculate and display average ratings.
- **Recommendations**: Basic recommendation system based on genres or user ratings.
- **Pagination**: Pagination for lists of books and reviews.
- **API Documentation**: Automatically generated using `drf-yasg` and accessible via Swagger UI.

## Tech Stack

- **Backend**: Python with Django
- **API Framework**: Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: JWT Authentication via `djangorestframework-simplejwt`
- **Documentation**: Swagger UI using `drf-yasg`
- **ORM**: Django ORM

## Installation Guide

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package installer)

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   
   git clone https://github.com/prudhvi-1618/BookReviewAPI.git
   cd BookReviewAPI
   ```
 2. **Install Dependencies**
     ```bash
     
       pip install -r requirements.txt
     ```  
 3.  **Set Up PostgreSQL Database**
     ```bash
       pip install -r requirements.txt
      ```
        3.1. **Create a Database for the Project**
      ```bash
         psql -U postgres
         CREATE DATABASE book_review_api;
      ```
        3.2. *Update Database Settings.*
        
        ```bash
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'book_review_api',
                'USER': 'postgres',  # Replace with your PostgreSQL username
                'PASSWORD': 'password',  # Replace with your PostgreSQL password
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```
   4. **Apply Migrations**
      ```bash
         python manage.py migrate
      ```
  5.**Running the Development Server**
     ```bash
       python manage.py runserver
    ```
# API Endpoints

## User Authentication:

- **`POST`** `/api/user/register/`: Register a new user.
- **`POST`** `/api/token/`: Login and retrieve a JWT token.

## Books:

- **`GET`** `/api/book/`: List all books.
- **`POST`** `/api/book/`: Add a new book.
- **`GET`** `/api/book/{id}/`: Get details of a specific book.
- **`PUT`** `/api/book/{id}/`: Update book details.
- **`DELETE`** `/api/book/{id}/`: Delete a book.

## Reviews:

- **`GET`** `/api/review/`: List all reviews for a book.
- **`POST`** `/api/review/`: Add a review for a book.
- **`PUT`** `/api/review/{review_id}/`: Edit your review.
- **`DELETE`** `/api/review/{review_id}/`: Delete your review.

## Recommendations:

- **`GET`** `/api/book/recommendations/`: Get book recommendations based on genres or ratings.

---

### Note:

Ensure you have proper authentication for the endpoints that require a JWT token. Pass the token in the `Authorization` header like this:

<pre style="background-color: #f5f5f5; border-radius: 5px; padding: 15px; font-family: 'Courier New', monospace; overflow-x: auto;">Authorization: Bearer &lt;your_jwt_token&gt;</pre>
  
