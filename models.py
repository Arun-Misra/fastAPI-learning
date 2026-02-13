from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    desc: str
    price: float
    quantity: int

    # def __init__(self, 
    # id: int,
    # name: str,
    # desc: str,
    # price: float,
    # quantity: int):
    #     self.id=id
    #     self.name= name
    #     self.desc=desc
    #     self.price= price
    #     self.quantity= quantity