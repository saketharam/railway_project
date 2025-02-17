# workindia irctc
# Railway Management System API

## Overview
This is a **Django-based Railway Management System API** that allows users to:
- Register and log in
- Check train availability
- Book train tickets with **race condition handling**
- Admin functionalities for train management

## Tech Stack
- **Backend**: Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: Token-based authentication

## Installation & Setup

### 1. Clone the Repository
```sh
git clone <repo-link>
cd railway-management-system
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database
Modify `settings.py` with your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional for Admin)
```sh
python manage.py createsuperuser
```

### 7. Run the Server
```sh
python manage.py runserver
```

## API Endpoints

### **User APIs**
- **Register**: `POST /api/users/register/`
- **Login**: `POST /api/users/login/`

### **Train APIs** (Admin Only)
- **Add Train**: `POST /api/trains/add/`

### **Booking APIs**
- **Book a Seat**: `POST /api/bookings/book/`

## Authentication
- Users must **register and log in** to get an authentication token.
- Include the token in the `Authorization` header for protected endpoints.

## Running Tests (Optional)
```sh
python manage.py test
```





