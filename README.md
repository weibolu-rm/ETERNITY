# ETERNITY
Calculator implementation from scratch

![poster](https://user-images.githubusercontent.com/10562703/128573357-ddb20ba3-a0d7-4d74-b538-6d6854112d86.png)

## How to run project
Prerequites: have python and node.js installed

### Set up python's virtual environment
```
$ pipenv install --dev 
$ pipenv shell
```

alternatively using python3 virtualenv

```
$ virtualenv -p python3 venv
$ source venv/bin/activate

$ pip install -r requirements.txt
```

### Set up vue cli
```
$ sudo npm install -g @vue/cli
```

### Install jQuery
```
$ cd frontend
$ npm install jquery
```

### Run backend
```
$ cd backend
$ python manage.py migrate
$ python manage.py runserver
```

### Run frontend
```
$ cd frontend
$ npm install
$ npm run serve
```
Vue server will be listening on http://localhost:8080/
