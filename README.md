# POKT TOOL PY


This is an experimental project to manipulate the information of the nodes of the POKT network
### DATA SOURCES:
- EXPLORER: [POKT WATCH EXPLROER](https://pokt.watch/)

- RPC POKT NODE: [API DOC](https://docs.pokt.network/api-docs/pokt/#/)



## Installation

Install with pip:

```
$ pip install -r requirements.txt
```



## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server. 

JSON_SORT_KEYS : By default Flask will serialize JSON objects in a way that the keys are ordered.


 
## Run Flask
### Run flask for develop
```
$ python webapp/run.py
```
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000/api/v1/docs`


## First Time creating image on docker

### Build image
```
$ docker-compose build
```

or in production

```
$ docker-compose -f docker-compose.prod.yml build
```

### Finally, run the app using the next command 
```
$ docker run -p 5000:5000 --name starport starport 
```


In image building, the webapp folder will also add into the image


### Run with Docker

```
$ docker build -t starport .
```

or 

```
$ docker-compose up 
```


## Changelog


- Version 1.0 : Base backend of the project 

-- JWT Tokens
-- SQLALCHEMY
-- MIGRATIONS
-- SWAGGER DOCS