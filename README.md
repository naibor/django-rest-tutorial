##### django rest framework tutorial
### set up environment
- Create a new virtual env.
`python3 -m venv env`
- Activate it
`source env/bin/activate`
- Install requirements
`pip install django`
`pip install djangorestframework`
`pip install pygments`  # We'll be using this for the code highlighting
- Get started
- Create a new project and cd into it
`django-admin startproject tutorial`
`cd tutorial`
- Create an app that we'll use for the simple web api
`python manage.py startapp snippets`
- Add the new app snippets and rest_framework to INSTALLED_APPS in settings.py
- Create models for your app
- Create an initial migration for your model and sync with the database
`python manage.py makemigrations snippets`
`python manage.py migrate snippets`
- Remember to make migrations before running server
`python manage.py migrate`
- To run server do,
`python manage.py runserver`
- To test the server, we will use httpie
- To install
`pip install httpie`

