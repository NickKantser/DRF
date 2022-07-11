# API
## Installation (For Linux/Mac)
First of all create a virtual environment in the root folder(where is requirements.txt file)
```sh
python3 -m venv .venv
```
and activate it
```sh
source .venv/bin/activate
```
##### *All the following commands are run from the virtual environment*
After that install all requirements:
```sh
pip3 install -r requirements.txt
```
Go to the folder where the manage.py file is located and run the following:
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
Once the migration is done you can run the server:
```sh
python3 manage.py runserver
```

## URLS
**To create record in the database use *YOURSERVERADDRES/import/* url**

> You can pass array of dictionaries to create multiple records on once or pass only dictionary

For example:
```json
[
  {
    "AttributeName": {
      "id": 1,
      "nazev": "Barva"
    }
  },
  {
    "AttributeValue": {
      "id": 1,
      "hodnota": "modrá"
    }
  }
]
```
or just
```json
{
    "AttributeName": {
      "id": 1,
      "nazev": "Barva"
    }
}
```

**To get all records of specific model go to *YOURSERVERADDRES/detail/MODELNAME/* or to get specific record of specific model go to *YOURSERVERADDRES/detail/MODELNAME/ID/***