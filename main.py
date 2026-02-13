from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my Server"

products = [
    Product(id=1,name= "phone",desc= "budget phone",price=99,quantity= 10),
    Product(id=2,name= "laptop",desc= "gaming laptop", price= 992,quantity= 23)
    # Product(2,"laptop","gaming laptop",992,23)
]
@app.get("/app")
def hehe():
    return "HEHEHEHhe"

@app.get("/products")
def get_all_products():
    return products
