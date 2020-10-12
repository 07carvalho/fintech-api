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

Then:
> docker-compose up -d

Backend service will be available in:

[http://localhost:8000](http://localhost:8000)

## Documentation
The API documentation is available in:

[http://localhost:8000/docs](http://localhost:8000/docs)

## Testing
To test the backend service, run:
> docker-compose run api python3 manage.py test base
