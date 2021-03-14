# FIFA 21 API
The REST API is written in Django for FIFA 21

## Overview

**Below**: *Screenshot from the browsable API*

![alt text](/assets/image/overview.png "Browsable API")


## Technologies used
* [Django Rest Framework](https://www.django-rest-framework.org): Django REST framework is a powerful and flexible toolkit for building Web APIs.


## Installation
* If you want to run the REST API, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* Then, clone the repo to your PC
    ```bash
        $ git clone https://github.com/othmbela/fifa-21-api.git
    ```


* #### Dependencies
    1. Cd into your the cloned repository as such:
        ```bash
            $ cd fifa-21-api
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python3 -m venv venv
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the documentation on your browser by using
    ```
        http://localhost:8000
    ```


# Files and Folders structure

```
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── assets
│   └── images
├── settings
│   └── settings.py
├── utils
│   ├── fields.py
│   └── pagination.py
├── api
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
└── apps
    ├── __init__.py
    ├── player
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── team
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── serializers.py
        ├── tests.py
        ├── urls.py
        └── views.py
```

## Author

**Othmane Belarbi**
