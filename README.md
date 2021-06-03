# ETERNITY
Calculator implementation from scratch

## How to run project
Prerequites: have python and node.js installed
### Set up python environment
```
$ pipenv install --dev
$ pipenv shell
```
### Set up django and vue cli
```
$ pip install django
$ sudo npm install -g @vue/cli
```

### Run backend
```
$ cd backend
$ python manage.py migrate
$ python manage.py runserver
```
Django server will be listening on http://127.0.0.1:8000/

### Run frontend
```
$ cd frontend
$ npm install
$ npm run serve
```
Vue server will be listening on http://localhost:8080/