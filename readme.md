# kenefit

to run my version of code 
run these commands:
1. pip install virtualenv
2. virtualenv my_name
3. my_name\scripts\activate  (-- this runs the virtual environment)
4. pip install -r requirements.txt
5. make postgres db and add your db info at django settings at DATABASES variable ("you may follow along this blog https://www.geeksforgeeks.org/how-to-use-postgresql-database-in-django/")
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver