from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated
from datetime import date,time #
import pymongo



"""fake db it list now which store data"""
d = []

""" User class which has dates, times, message variable.
User class inherit BasedModel class"""
class User(BaseModel):
     dates : date|None = None
     times : time|None = None
     message :str |None = None

"""Creating app object or create a instance of FastApi class"""
app = FastAPI()


"""write now be are creating fake data base But
    be can used Sql or Mongodb for this process. """
def database(data: dict):
    d.append(data)

"""a.post decorator is used implement the necessary properties of app"""
@app.post('/set')
def set_reminder(reminder : User):
    data = reminder.dict()
    database(data=data)
    return {'massage' : 'successful set!'}

@app.get('/reminder')
def get_reminder():
    return d
#uvicorn filename:app
#http://127.0.0.1:8000/doc 