# Read me

# Created as a test project to Order Wedding Bouquets.

If you wish to clone this project and run the project on your machine please follow the instructions below. 

## Installing

### Requirements

In this project I am using python version is 3.9.5 and default db.sqlite3 

#### For macOS
If you don't have it, install the python and django other extra requirments.
Link for the python documentation : https://docs.python.org/3/
Link for the Django documentation :https://docs.djangoproject.com/en/3.2/


### Virtual environment
Create a virtual environment with python 3.9.5.

To create virtual enviorment : `python3 -m venv (folder_name_here)`
to Activate the virtual enviorment run : `source (folder_name_here)/bin/activate`

Then run `pip install -r requirements.txt`


#### Database setup

In another terminal, run the following command to set up your admin user.
- `python manage.py createsuperuser`

This is only a local database, so don't worry about password security. 
You can enter something like email: something@gmail.com, pwd: ****


**In the same terminal**, then run, replacing <current_migration> with the number for the **the latest committed migration file**:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py migrate flower <last_commited_migration>` 
- `python manage.py migrate`

To see all available and applied migrations, you can run
- `python manage.py showmigrations`


## Deployment

### Local (for developing)

To run the following commands in one terminal: But first make sure you are inside the project(Order_app) directory.
Then run - `python manage.py runserver`

The logs will show in your first terminal.

You can access the platform through http://localhost:8000/


Once you've updated your code, simply stop and run the WEB service by running these two commands on another terminal:


#### Google OAuth Setup

Go to http://0.0.0.0:8000/admin as a superuser to the Sites section.
Edit www.example.com to be localhost.

Then go to the **Social Applications section** and add a new **social application**. 
Choose Google provider and enter the following credentials:
- Client id: `225391600233-ct5v9lls215kpi2rs9lh87337th2h2fo.apps.googleusercontent.com`
- Secret key: `PaD9pL1e3H4NDEqd8Kr16A3o`

On Authorized JavaScript origins, add the following URIs:
- http://localhost:8000
- http://127.0.0.1:8000

On Authorized redirect URIs add the following URIs:
- http://localhost:8000/accounts/google/login/callback/
- http://127.0.0.1:8000/accounts/google/login/callback/



You can only commit the new migration files if **all changes are applied, rollback and re-applied successfully**.

*Be warned that if testing migration fails it will indicate that you did not follow this procedure correctly!*


### Static files

Some static files such as images may not update automatically inside the container.
