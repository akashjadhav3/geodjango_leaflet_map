# geodjango_leaflet_map
- Using weather.gov API show Weather Forcast in map using (python, django, Geodjango, leaflet.js, postgis)

![Image of Weather app](/weather_app_screenshot.png)
show weather forecast using geodjango, leafletjs and posgis using.
### Install requirements for the project:
- for Linux 
   `sudo pip3 install -r requirements`
   
#### Install Postgresql & configure Extension Postgis
After Installing PostgreSql
- Create extension postgis
1. Install Postgis
```python apt-get install postgis```
2. open postgres
`sudo su - postgres`
* Then Type
`psql`
3. Create Database
`CREATE DATABASE <db_name>;`
4. Connect/use database
`connect <db_name>;`
5. Create Extension Postgis
`CREATE EXTENSION postgis;`
#### Migrate database
`python manage.py makemigrations`

```python manage.py migrate```

#### Run Project
`python manage.py runserver`

#### Adding City and Location
- create superuser and login to Django Admin
`python manage.py createsuperuser`
- After that login and click Cities and add city and location
