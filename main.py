from fastapi import FastAPI
from models import Product
from database import session, engine
import database_model
app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

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

# Populate database with initial products if empty
db = session()
if db.query(database_model.Product).count() == 0:
    for prod in products:
        db_product = database_model.Product(id=prod.id, name=prod.name, desc=prod.desc, price=prod.price, quantity=prod.quantity)
        db.add(db_product)
    db.commit()
db.close()

@app.get("/")
def greet():
    return "Welcome to my Server"

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
    db = session()
    db_products = db.query(database_model.Product).all()
    db.close()
    return db_products
# @app.get("/products")
# def get_all_products():
#     return products

@app.get("/product/{id}")
def get_prod_by_id(id:int):
    db = session()
    product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    db.close()
    if product:
        return product
    return {"message": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    db = session()
    db_product = database_model.Product(id=product.id, name=product.name, desc=product.desc, price=product.price, quantity=product.quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return {"message": "Product added successfully", "product": db_product}

@app.put("/product/{id}")
def update_product(id: int, product: Product):
    db = session()
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.desc = product.desc
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)
        db.close()
        return {"message": "Product updated successfully", "product": db_product}
    db.close()
    return {"message": "Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int):
    db = session()
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        db.close()
        return {"message": "Product deleted successfully"}
    db.close()
    return {"message": "Product not found"}