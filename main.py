from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read_root():
    return { "message" : "hello from FastApi"}

@app.get('/greet')
def greet():
    return {"message" : "Hello Aziz"}


# example of path parmeter
@app.get('/greet/{name}')
def greet_name(name: str):
    return {"message": f"Hello.. {name}"}

# example of path parmeter
@app.get('/greet/{id}')
def greet_name(id: int):
    return {"message": f"Hello.. {id}"}


#example of query parameter
@app.get('/intro/{name}')
def greet_name(name: str, age: Optional[int] = None):
    return {"message": f"Hello.. {name} you are {age} years old..."}

#example of query parameter
@app.get('/intro')
def greet_name(name: str, age: Optional[int] = None):
    return {"message": f"Hello.. {name} you are {age} years old..."}

# time: 37:20