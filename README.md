

## Build
### DB
 - docker build -t djdb:1 infra/db
 - docker run -dit -p 3306:3306 --name=django2_db djdb:1

## Run app
 - manage makemigrations
 - manage migrate
 - manage runserver