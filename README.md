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