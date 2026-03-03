from fastapi import FastAPI
from model import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Yokoso watashino master wayne"

products = [
    Product(id = 1, name="gba",description= "budget one", price=79, quantity=10),
    Product(id = 2, name= "nds", description = "average price",price= 120,quantity= 34)
]


@app.get("/products")
def get_all():
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