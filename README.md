# Bradfield Takehome - Exercise 3 - Time zones

## About
This project ...

## System setup 
This project is written in Python3

To prepare your system to run this project I ran: 

1. `mdkir bradfield_takehome_exercise3`
2. `cd bradfield_takehome_exercise3`
3. initiate virtualenv: `python3 -m venv venv`
4. activated virtualenv: `. venv/bin/activate`
5. `mkdir wallclock`

To run on your machine: 

1. `cd bradfield_takehome_exercise3`
2. `pip install -e .`

To run the app:

1. `cd bradfield_takehome_exercise3`
2. `export FLASK_APP=timezone`
3. `export FLASK_ENV=development`
4. `flask run`
5. In separate terminal `curl -i -H "Content-Type: application/json" -X POST -d '{"tz":"America/Los_Angeles"}' http://127.0.0.1:5000/wallclock/api/v1.0/time`

To run testes:

1. `cd bradfield_takehome_exercise3`
2. `pytest`

## Helpful resources 
* [Flask official docs](https://flask.palletsprojects.com/en/1.1.x/)
