from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my Server"

products = [
    Product(id=1, name="phone", desc="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", desc="gaming laptop", price=992, quantity=23),
    Product(id=3, name="headphones", desc="wireless noise-cancelling headphones", price=199, quantity=15),
    Product(id=4, name="smartwatch", desc="fitness tracking smartwatch", price=299, quantity=8),
    Product(id=5, name="tablet", desc="10-inch Android tablet", price=349, quantity=12),
    Product(id=6, name="mouse", desc="ergonomic wireless mouse", price=49, quantity=25),
    Product(id=7, name="keyboard", desc="mechanical gaming keyboard", price=129, quantity=18),
    Product(id=8, name="monitor", desc="27-inch 4K monitor", price=499, quantity=6),
    Product(id=9, name="printer", desc="all-in-one inkjet printer", price=179, quantity=9),
    Product(id=10, name="router", desc="Wi-Fi 6 mesh router", price=249, quantity=14),
    Product(id=11, name="external drive", desc="2TB portable SSD", price=149, quantity=20),
    Product(id=12, name="webcam", desc="1080p HD webcam", price=79, quantity=16),
    Product(id=13, name="microphone", desc="USB condenser microphone", price=89, quantity=11),
    Product(id=14, name="speakers", desc="2.1 channel computer speakers", price=69, quantity=22),
    Product(id=15, name="charger", desc="fast charging power bank", price=39, quantity=30),
    Product(id=16, name="case", desc="protective phone case", price=19, quantity=40),
    Product(id=17, name="stand", desc="adjustable laptop stand", price=59, quantity=17),
    Product(id=18, name="cable", desc="USB-C to HDMI cable", price=29, quantity=35),
    Product(id=19, name="adapter", desc="universal travel adapter", price=24, quantity=28),
    Product(id=20, name="dock", desc="multi-port USB dock", price=89, quantity=13)
]

ic = []
for i in range(len(products)):
    ic.append(products[i].id);

def binary(lis, d):
    if not lis:
        return False
    l = 0
    r = len(lis) - 1
    while l <= r:
        mid = l + (r - l) // 2 
        if d == lis[mid]:
            return True
        elif d < lis[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return False

@app.get("/app")
def hehe():
    return range(20)

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_prod_by_id(id:int):
    if binary(ic,id):
        return products[id-1]
    return "Not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}
