# HMS-API
[![CircleCI](https://circleci.com/gh/D-Kamunya/hms_api/tree/master.svg?style=svg)](https://circleci.com/gh/D-Kamunya/hms_api/tree/master)

[![codecov](https://codecov.io/gh/D-Kamunya/hms_api/branch/master/graph/badge.svg?token=1UEY3WQNB1)](https://codecov.io/gh/D-Kamunya/hms_api)

## Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)


## Installing
### Setting up the database
- Start your database server and create your database

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/D-Kamunya/hms_api.git) `git clone https://github.com/D-Kamunya/hms_api.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv name_of_your_virtual_environment`
- Create a .env file and put these key=values in it:
```
source name_of_your_virtual_environment/bin/activate
export DEBUG=True
export DB_NAME="your_db_name"
export DB_USER="your_postgres_username"
export DB_PASSWORD="your_postgres_password"
export DB_HOST="localhost or any other host name"
export DB_PORT="port_number"
export SECRET_KEY=''
export SENDGRID_API_KEY=''
export EMAIL_HOST_USER=''
export EMAIL_HOST=''
export EMAIL_PORT=587
export MODE=''
export ALLOWED_HOSTS=''
export DISABLE_COLLECTSTATIC=1
export DOMAIN='http://127.0.0.1:8000'
export UIDOMAIN='http://127.0.0.1:4200'
export PUB_KEY=''
export SECRET=''
export CLOUD_NAME=''
export API_SECRET=''
export API_KEY='' 
export EMAIL_USE_TLS=True 

```
- Load the environment variable `source .env`
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`
