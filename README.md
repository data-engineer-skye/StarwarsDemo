
# StarWars API Demo

## Project Goals
---
Using Star Wars API  
Design an automation script to answer following questions.

1. How many different species appears in film-6 (Revenge of the Sith) ?
2. Please list all the film names and sort the name by episode_id.
3. Please find out all vehicles which max_atmosphering_speed is over 1000.

## Requirements
---
Before you begin, ensure you met the following requirements:  
* You have installed Python3, written in Python 3.8.10
* You have installed allure (if you want to check allure report)
    ```
    brew install allure
    ```
   

## Create Python3 Venv
---
Create new venv
```bash
$ python3 -m venv starwars_venv
```
Acitvate venv
```bash
$ source starwars_venv/bin/activate
```

## Installation
---
```bash
$ pip3 install -r requirements.txt
```

## Example Run Test
---
Run all tests under test_api
```bash
$ pytest test_api
```
Run specific quesion
```bash 
$ pytest test_api/test_question1.py
```
---

## Easy Setup and Run
Script includes create venv, install requirements, and run all tests under test_api
```
$ bash run_tests.sh
```

---

## Check Allure Report
```
$ allure serve reports
```

## API Documentation
---
https://swapi.py4e.com/documentation


