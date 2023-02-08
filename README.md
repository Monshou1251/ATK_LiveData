## ATK_LiveData

---

### Project overview:

ATK_LiveData is a webportal that provides such functions as creating, reading, updating and deleting data from PostgreSQL database.
Frontend side of the project is done with VueJS tools on pure JavaScript with basic HTML and CSS. Server side manipulations and functions are maintained with Django framework written on python.

---

### How to deploy the project:

Firstly, download and install python (v 3.8.10 recommended):

```
https://www.python.org/downloads/release/python-3810/
```

Download and install node.js (it will be required to run vue part of the project):

```
https://nodejs.org/en/
```

Make sure to have installed Git on your machine:

```
https://git-scm.com/download/
```

For testing purposes create test tables in your postgresql database by using scripts from ATK_LiveData/Test_data/create_tables.sql and imoprt the provided data from csv. files from the same folder.
If you don't have postgresql on your machine, it could be downloaded through the link below:

```
https://www.postgresql.org/
```

Now it is required to deploy the backend part of the project.
Clone the repository:

```
git clone https://github.com/Monshou1251/ATK_LiveData.git
```

Go to project directory:

```
cd ATK_LiveData
```

Create and activate the virtual enviroment:

```
python -m venv venv

```

```
. venv/scripts/activate
```

Upgrade (or install) pip:

```
python -m pip install --upgrade pip
```

Go to backend folder:

```
cd backend
```

Install requirements from requirements.txt:

```
pip install -r requirements.txt
```

To connect django with the database the settings file should be adjusted.
Go to

```
ATK_LiveData/backend/drestapi/settings.py
```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',         # Your name of database rigestered in postegresql
        'USER': 'postgres',         # Your username rigestered in postegresql
        'PASSWORD': 'postgres',     # Your password rigestered in postegresql
        'HOST': 'localhost',        # Your adress where postgresql db is located
        'PORT': '5432',
    }
}
```

Make migrations:

```
python manage.py migrate
```

Run django:

```
python manage.py runserver
```

Now we need to deal with frontend.
Go back in a main folder

```
cd ..
```

Then to frontend folder:

```
cd frontend
```

Install npm (it will include all node_modules):

```
npm install
```

Now Vue is ready to be started:

```
npm run serve
```

---

## Tech

ATK_LiveData uses a number of open source projects to work properly:

- [Python] - a programming language that lets you work quickly and integrate systems more effectively.
- [Django] - a high-level Python web framework
- [JavaScript] - JavaScript is the world's most popular programming language
- [Vue] - the progressive JavaScript framework

---

## Authors

- Monshou1251

---
