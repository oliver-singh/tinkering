from fastapi import FastAPI
from app.utils import add

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Azure!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}