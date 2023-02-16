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

SECRET_KEY=!!!ENTER_YOUR_SECRET_KEY!!!
DEBUG=True

*  Install docker composer and run command:
docker-compose up

* Create django superuser:
python manage.py createsuperuser
 
* You may create normal user for testing the app, however, admin is also fine.

* Create Tier objects in admin for 3 plans:
  * Basic, name=”basic”, Thumbnail size = 200
  * Premium, name=”premium”, Thumbnail size = 200, 400, link_orig = True
  * Enterprise, name=”enterprise”, Thumbnail size = 200, 400, link_orig = True, link_expir = True

## Summary

Time necessary to prepare this simple app was around 3 working days.

Please consider that up to now I’ve worked in a clean Django and I don’t have experience with the REST framework. The most time consuming for me was to prepare tests, which are not perfect and should be improved.
