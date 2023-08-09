# My python APi

### Steps:
* python3 -n venv venv ==> create the venv env
* source venv/bin/activate ==> to activate the venv
* any pip command will not be installed in this new env
* to deactivate the venv
* install flas: pip install flask

* create the app.py flask API

* export FLASK_APP=app
* export FLASK_ENV=development 

* how to run: python app.py

* capture the requirement in txt == > pip freeze > requirements.txt

* Add Docker file

* run docker build and tag and run and push
docker build -t my-flask-api:v1 .
docker images | grep "flask"
docker run -p5001:5000 my-flask-api 
docker tag my-flask-api:v1  333743/my-flask-api:v1
docker push 333743/my-flask-api:v1

* can be seen here: https://hub.docker.com/r/333743/my-flask-api
