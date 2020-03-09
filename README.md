# Overview

This project is to create a prototype REST API in python to support the product feature.

# Quick start

  - Create and activate virtualenv for this project
```sh
   $ virtualenv -p python3 venv (do this only one time)
   $ source venv/bin/activate
```
  - Install necessary packages from requirements.txt
```sh
   $ pip install -r requirements.txt
```
  - Migrate app, create superuser and run project.
```sh
   $ python manage.py migrate
   $ python manage.py createsuperuser (this is for creating admin user. do this only one time)
   $ python manage.py runserver (To do unit tests, please don't run this command)
```
  - Project will run on http://127.0.0.1:8000/
  
# API Information

/ Request Method | Endpoints | Description |
| ------ | ------ | ------ |
| GET | /api/v1/questions/ | Display all questions in a list |
| GET | /api/v1/questions/<question_id>/ | Display detailed information of specific question |
| GET | /api/v1/questions/answers/ | Display all answers about any questions in a list |
| GET | /api/v1/questions/answers/<answer_id> | Display detailed information of specific answer |
| GET | /api/v1/questions/<question_id>/answers/ | Display all answers about specific question |
| POST | /api/v1/questions/ | Create question ( or questions ) |
| POST | /api/v1/questions/answers/ | Create answers with questions |

# Request & Response Example

## POST /api/v1/questions/

Example: POST http://localhost:8000/api/v1/questions/

Request body:
```
[
    {
        "posted_user": 1, // This is id of specific user
        "questions": "Test questions1",
        "book_mark": 0
    }, {
        "posted_user": 1, // This is id of specific user
        "questions": "Test questions2",
        "book_mark": 1
    }
]
```
Successful Response - 201:
```
[
    {
        "id": 1,
        "questions": "Test questions1",
        "book_mark": 0,
        "posted_user": 1
    },
    {
        "id": 2,
        "questions": "Test questions2",
        "book_mark": 1,
        "posted_user": 1
    }
]
```

## POST /api/v1/answers/

Example: POST http://localhost:8000/api/v1/answers/

Request body:
```
[
    {
        "answered_user": 1, // This is id of answered user
        "question": 1, // This is id of specific question
        "answers": "This is answer about question11",
        "book_mark": 0
    }, {
        "answered_user": 1, // This is id of answered user
        "question": 1, // This is id of specific question
        "answers": "This is answer about question12",
        "book_mark": 0
    }, {
        "answered_user": 1, // This is id of answered user
        "question": 2, // This is id of specific question
        "answers": "This is answer about question21",
        "book_mark": 1
    }
]
```
Successful Response - 201:
```
[
    {
        "id": 5,
        "answers": "This is answer about question11",
        "book_mark": 0,
        "answered_user": 1,
        "question": 1
    },
    {
        "id": 6,
        "answers": "This is answer about question12",
        "book_mark": 0,
        "answered_user": 1,
        "question": 1
    },
    {
        "id": 7,
        "answers": "This is answer about question21",
        "book_mark": 1,
        "answered_user": 1,
        "question": 2
    }
]
```

# Unit Tests
  - Please make sure you ran all commands right before `python manage.py runserver` in `Quick Start` in above
  - Run unit tests by running following commands.
```sh
   $ python manage.py test
```