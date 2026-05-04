from fastapi import FastAPI
from database import session, engine
from model import Product
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "Yokoso watashino master wayne"


def init_db():
    db = session()

    for product in products:
        db.add(database_models.Product(**product.model_dump))
init_db()

products = [
    Product(id = 1, name="gba",description= "budget one", price=79, quantity=10),
    Product(id = 2, name= "nds", description = "average price",price= 120,quantity= 34)
]


@app.get("/products")
def get_all():
    db = session

    return products   # in url use /products after localhost link


@app.get("/product-id/{id}")
def getman(id : int):
    for product in products:
        if product.id == id:  
            return products[id]
        
    return "Not found master"

@app.post("/product")
def add_product(product : Product):     #here Product is a class
    products.append(product) 
    return product           #whereas product is a variable of Class Product


@app.put("/product")
def add_product(id : int, product : Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added successfully"
    return "Product not found man"

@app.delete("/product")
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
    return "No product like that exists"