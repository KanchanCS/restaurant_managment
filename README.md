# Restaurant Managment  
## Summary
https://github.com/user-attachments/assets/377485cc-3751-4ea7-bd8e-328b19c678df
#### This is a full-featured Django-based web application built for Madu Restaurant, featuring an elegant and responsive design. It includes a dynamic menu system, an online order platform, and a blog where restaurant owners can share posts about their services, events, and promotions. The website also includes a customer login and registration.
## Installation
* Clone the repository:
  ```python
  git clone https://github.com/KanchanCS/madu-restaurant.git
  ```
* Create a virtual environment:
  ```python
   python -m venv venv
  ```
* Activate the virtual environment:
  - On Windows:
    ```python
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```python
    source venv/bin/activate
    ```
* Install dependencies:
  ```python
  pip install -r requirements.txt
  ```
* Run migrations to set up the database:
  ```python
  python manage.py makemigrations
  python manage.py migrate
  ```
* Create a superuser to access the Django admin panel:
  ```python
  python manage.py createsuperuser
  ```
* Start the development server:
  ```python
  python manage.py runserver
  ```
* Open your browser and go to http://127.0.0.1:8000/ to view the website.

 ## Usage
 * Admin Panel: Log in at http://127.0.0.1:8000/admin with your superuser credentials to manage  menu items, blog posts, and orders.
 * Blog: Add blog posts in the admin panel or directly from the frontend form (if authenticated).
 * Order Management: Customers can place orders from the menu, and admins can view and manage them in the dashboard.
