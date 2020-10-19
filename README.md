# Bradfield Takehome - Exercise 3 - Time zones

## About
This project implements an api with a single endpoint to return the 
server wall-clock time (see [Google sheet](https://docs.google.com/document/d/1F-eGgUg6_c0UZuk0HssdgZLyPe9k1zeEeCdCs-tGaWA/edit?usp=sharing) for more information). The client
can also specify an optional timezone parameter, which will output 
the current time in that timezone. 

## System setup 
This project is written in Python3.

To prepare your system to run this project:

1. Verify you have Python3 installed: `python3 --version`
2. If not, install: `brew install python` 
3. Save this project anywhere and `cd bradfield_takehome_exercise3`
4. Initiate a virtual env: `python3 -m venv venv`
2. Activate the virtual env `. venv/bin/activate`
4. Install the project in the virtual env `pip install -e .`


## Run the app locally

1. Navigate to the project root: `cd bradfield_takehome_exercise3`
2. Export the app name environment variable: `export FLASK_APP=timezone`
3. If developing, export the development environment variable: `export FLASK_ENV=development`
4. Run the app: `flask run`

## Send requests to local server:

```bash
# Valid request - valid timezone - returns 200
curl -i -H "Content-Type: application/json" -X POST -d '{"tz":"America/Los_Angeles"}' http://127.0.0.1:5000/wallclock/api/v1.0/time

# Valid request - no timezone - returns 200 
curl -i -H "Content-Type: application/json" -X POST -d '{}' http://127.0.0.1:5000/wallclock/api/v1.0/time

# Inalid request - invalid timezone - returns 400 
curl -i -H "Content-Type: application/json" -X POST -d '{"tz": Space/Mars}' http://127.0.0.1:5000/wallclock/api/v1.0/time

```

## Run unit tests

1. Navigate to the project root: `cd bradfield_takehome_exercise3`
2. Run tests: `pytest` 

## Future work / shortcomings 
* Implement more informative error messaging
* Add more meaningful tests and improve coverage
* Better understand datetime vs. time package

## Helpful resources 
* [Flask official docs](https://flask.palletsprojects.com/en/1.1.x/)
