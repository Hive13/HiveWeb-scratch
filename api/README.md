# Hive13 API

### Dependencies
- Flask:        v1.1.1
- flask-rest:   v0.3.7
- markdown:     v3.1.1

### Run it
1. `docker-compose build`
2. `docker-compose up`
    - this launches on `http://localhost:8000`

### Current Endpoints
* `/` shows this README as HTML page
* `/test` responds with a json response (works in browser or with postman)