# Hive13 API

### Dependencies
- markdown:             v3.1.1
- Flask:                v1.1.1
- sqlalchemy            v1.3.13
- sqlalchemy-citext:    v1.3.post0
- pg8000:               v1.13.2

### Run it
1. `docker-compose build`
2. `docker-compose up`
    - this launches on `http://localhost:8000`

### Future Considerations
1. Remove `flask-rest` dependency
  * It's cumbersome, and adds bloat, can get the same thing with just bare flask


### Current Endpoints
* `/` shows this README as HTML page
* `/test` responds with a json response (works in browser or with postman)