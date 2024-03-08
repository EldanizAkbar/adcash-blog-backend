# Adcash Blog Backend

Welcome to the Adcash Blog Backend repository! This project contains the backend code for a simple blog website built with Django. The API allows users to manage categories and posts for the blog.

## Features

- CRUD operations for categories (Create, Read, Update)
- CRUD operations for posts (Create, Read, Update, Delete)
- Retrieve lists of categories and posts
- Filter posts by categories

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/adcash-blog-backend.git

2. Create a virtual environment (recommended):

   ```bash
   python -m venv env

3. Activate the virtual environment:       

   ```bash
   .\env\Scripts\activate
   
4. Install dependencies:

   ```bash
   pip install -r requirements.txt

5. Apply migrations:

   ```bash
   python manage.py migrate

6. Create default categories:

   ```bash
   When you run migrations, the default categories (Sport, Education, Science) will be created automatically.
   
7. Run the development server:

   ```bash
   python manage.py runserver



## API Endpoints

- ```GET /api/categories/:```  Get a list of all categories.
- ```POST /api/categories/:``` Create a new category. (Requires name field in the request body)
- ```GET /api/posts/:``` Get a list of all posts.
- ```POST /api/posts/:``` Create a new post. (Requires title, content, and categories fields in the request body)
- ```GET /api/posts/<int:pk>/:``` Get details of a specific post by ID.
- ```PUT /api/posts/<int:pk>/:``` Update details of a specific post by ID. (Requires title, content, and categories fields in the request body)
- ```DELETE /api/posts/<int:pk>/:``` Delete a specific post by ID.

##Testing

To run the unit tests for the API:

 ```bash
 python manage.py test
```

#Technologies Used

- Python
- Django
- Django REST framework
- PostgreSQL


















   
   
   
