# Local Library Website

This project is a Django-based web application that serves as an online catalog for a small local library. It allows users to browse available books and provides functionality for library management.

## Features
* Browse Books: Users can view a list of available books and detailed information about each book.
* Browse Authors: Users can view information about authors.
* Admin Interface: Admin users can create and manage models for books, book copies, genres, languages, and authors.
* Book Reservations (Future): The application is designed to be extended to allow users to reserve books.
* User Authentication: Support for user authentication will be added in future developments.
* Forms: The application will be extended to incorporate forms for various interactions.
* Librarian Functions (Future): Librarians can renew reserved books.

## Technologies Used
* Django Web Framework (Python)

## Get Started
To get this project up and running locally on your computer:

1. Set up the Python development environment. We recommend using the venv virtual environment.

2. Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python3 to start Python):
* pip3 install -r requirements.txt
* python3 manage.py makemigrations
* python3 manage.py migrate
* python3 manage.py collectstatic
* python3 manage.py test 
* python3 manage.py createsuperuser (**Make sure to remember your username and password. It is SUPER important**) 
* python3 manage.py runserver
<br/> <br/>

3. Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
4. Create a few test objects of each type.
5. Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
