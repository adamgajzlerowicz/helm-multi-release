# Automatically retire your kubernetes deployments

This is proof of concept on how to create new environments of your application on per-branch basis.

### Who is this for

This is an example that can be expanded on by developers to make it easy to deploy app on to separate environment using web interface.

### How this works
App uses helm for deploying charts. 
Key is that it will be re-deployed again and again but under a different chart name, which links it to originating branch.
This can be setup as a webhook or also added to the app.

# Configuration
* API relies on hosting machine to have access to the cluster.
* install api dependencies `pip3 install -r web-interface/requirements.txt`

## Release the app

* run `./release` script. This will deploy a test chart with bare nginx

## Access web interface

* run `env FLASK_APP=web-interface/index.py flask run` to start api
* open `web-interface/index.html` file

## Delete deployed chart

* from the web interface remove one of your charts

# TODO

* Add styles
* Show id address of services
* Allow creating environments from the interface
* dockerise the app
