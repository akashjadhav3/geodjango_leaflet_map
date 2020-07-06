# geodjango_leaflet_map
show weather forecast using geodjango, leafletjs and posgis using.
* Install requirements for the project:
for Linux 
   sudo pip3 install -r requirements
for Windows
   sudo pip3 install -r requirements
   
* Install Postgresql & configure Extension Postgis:
    After Installing PostgreSql
     How to create extension postgis
         1) Install Postgis
         #apt-get install postgis
         2) open postgres
         # sudo su - postgres
          Then Type
          #psql
         3) Create Database
         #CREATE DATABASE <db_name>;
         4) Connect/use database
         #connect <db_name>;
         5)Create Extension Postgis
         #CREATE EXTENSION postgis;
* Migrate database
#python manage.py makemigrations
#python manage.py migrate

* Run Project
#python manage.py runserver

 
