# Deployment

You can use [http://91.107.209.76:5000/](http://91.107.209.76:5000/) to test it on a VPS.

But for local you can continue with the steps below:

For using your python virtual environment, you can use
  
	python -m venv venv

to create a virtual environment. Moreover, for activating the virtual environment on Unix os, use :
  
	source venv/bin/activate

For running without docker you can use:

	cd web
	python manage.py runserver
  
For running test cases use:

	cd web
	python manage.py test web/tests
  
For running with docker you can continue with the steps below:
  
	docker build . -t docker-django-v0
	docker run docker-django-v0
