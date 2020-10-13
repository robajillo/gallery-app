### Gallery-App

#### Author  
  
[robajillo](https://github.com/robajillo)
  
#### Description  
This is a Django application for personal gallery that allows a user to upload images for others. Users can also search for images based on category.
  
####  Live Link  
 Click [View Site](https://gallery-application.herokuapp.com/)  to visit the site

 
#### User Story  
  
* View different  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
#### Setup and Installation  
To get the project .......  
  
#### Cloning the repository:  
 ```bash 
 https://github.com/robajillo/gallery-app.git 
```
#### Navigate into the folder and install requirements  
 ```bash 
cd gallery-app pip install -r requirements.txt 
```
#### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
#### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 #### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
#### Run the application  
 ```bash 
 python manage.py runserver 
``` 
#### Running the application  
 ```bash 
 python manage.py server 
```
#### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
#### Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  

#### Contact Information 

If you have any question or contributions, please email me at [rjillo@yahoo.com] or [rjillo259@gmail.com]

#### License
* *MIT License:*
* Copyright (c) 2020 **Roba Jillo**