from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my Server"

@app.get("/app")
def hehe():
    return "HEHEHEHhe"