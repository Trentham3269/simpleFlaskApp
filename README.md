# simpleFlaskApp

This repo steps through these detailed tutorials:
* [How to Get Started with Flask](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework)
* [Build a CRUD web app with Flask](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

### General setup
```
# Create and activate virtualenv
$ mkvirtualenv env1
$ workon env1

# Install Flask in project dir
$ pip install Flask

# Dependency manifest
$ pip freeze >> requirements.txt
```

### Run with
Try this:
```
$ export FLASK_APP=run.py
$ flask run
```
Or:
```
$ python run.py
```

### Port forwarding
As I am developing this app on a remote Ubuntu 16.04 instance I've used [this resource](https://www.saltycrane.com/blog/2012/10/how-run-django-local-development-server-remote-machine-and-access-it-your-browser-your-local-machine-using-ssh-port-forwarding/) to be able to view in Chrome on my machine:
* ```$ ssh -v -L 9000:localhost:5000 user@remoteserver``` on the local machine
* ```$ python run.py runserver 0.0.0.0:5000``` on the remote server
* View in the browser on the local machine at ```localhost:9000```


