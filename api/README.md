# Hive13 API

## Notes
* All endpoints are prefixed with `/api`

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
If you have any ides, put them here 😃

### Current Endpoints
* `/` shows this README as HTML page
* `/api/test` responds with a json response (works in browser or with postman)