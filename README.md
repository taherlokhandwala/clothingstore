# Clothing Web Site

Web Frameworks Project

Install git incase you dont have.

```
https://git-scm.com/download/
```

If you aren't familiar with git watch these 2 videos.

[Git Basics](https://www.youtube.com/watch?v=USjZcfj8yxE&t=78s)

[GitHub Basics](https://www.youtube.com/watch?v=nhNq2kIvi9s&t=3s)

Open cmd and Create a new virtual environment,install django and make a new project:

```python
virtualenv clothing
cd clothing/Scripts
activate
cd ..
pip install django
django-admin startproject clothing (Name the project clothing only.)
cd clothing
```

Now inside this clothing folder you will see another clothing folder.Delete only that folder.

After deletion do the following in cmd:

```python
git init
git remote add origin https://github.com/taherlokhandwala/clothing
git pull origin master
```

You should see a new clothing folder and a README.md.

Now with virtual environment activated do:

```python
python manage.py migrate
python manage.py runserver
```
