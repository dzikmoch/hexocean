## General info
This project was created as a recruitment task for HexOcean company.
Aim of the project was to write an API that allows user to upload an image in PNG or JPG format.

## Technologies
Project is created with:
* Docker-compose
* Django REST framework

## Setup
To run this project, please follow the steps below:
* Prepare .env file in the main directory consisting:
```python
SECRET_KEY=!!!ENTER_YOUR_SECRET_KEY!!!
DEBUG=True
```
*  Install docker composer and run command:
```bash
docker-compose up
```
*  Apply migrations:
```python
python manage.py makemigrations
python manage.py migrate
```
* Create django superuser:
```bash
python manage.py createsuperuser
```
* You may create normal user for testing the app, however, admin is also fine.

* Create Tier objects for 3 plans:
```python
Tier.objects.create(name="basic", thumbnail_size="200", link_orig=False, link_expir=False)
Tier.objects.create(name="premium", thumbnail_size="200, 400", link_orig=True, link_expir=False)
Tier.objects.create(name="enterprise", thumbnail_size="200, 400", link_orig=True, link_expir=True)
```
* In django-admin, go to the user object which you will use for the testing purpose. At the section "user profile" at end, assign one of the above tier.
* You are ready to start testing the project. Go to http://0.0.0.0:8000 

## Summary

Time necessary to prepare this simple app was around 3 working days.

Please consider that up to now I’ve worked in a clean Django and I don’t have experience with the REST framework. The most time consuming for me was to prepare tests, which are not perfect and should be improved.
