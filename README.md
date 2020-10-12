# dev-api-rest
Rest API for fintechs
Functionalities:
* Create account
* Block account
* Deposit transaction
* Check balance
* Withdraw
* List transactions (by order and date) 

Stack used:
* Python 3.8
* Django 2.2
* Django Rest Framework 3.11
* Postgres
* Docker


## Run locally
To run this application using Docker, run:
> docker-compose build

Create the database tables:
> docker-compose run api python3 manage.py migrate

Populate with a superuser and a user
> docker-compose run api python manage.py loaddata data.json

Then:
> docker-compose up -d

Backend service will be available in:

[http://localhost:8000](http://localhost:8000)

## Auth
Add an `Authentication` field with value `12345678900` in request header. For example:
> curl --location --request POST 'http://localhost:8000/api/v1/contas' \
--header 'Authorization: 12345678900' \
--header 'Content-Type: application/json' \
--data-raw '{
    "limiteSaqueDiario": 100,
    "tipoConta": 4
}'


## Documentation
The API documentation is available in:

[http://localhost:8000/docs](http://localhost:8000/docs)

## Testing
To test the backend service, run:
> docker-compose run api python3 manage.py test
