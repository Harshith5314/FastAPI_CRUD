from fastapi import FastAPI, Depends
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/") #home page
def greet():
    return "Hello World!"

products=[
    Product(id=1,name="Iphone",description="An IOS device",price=150000,quantity=3),
    Product(id=2,name="Samsung",description="An Android device",price=75000,quantity=4),
    Product(id=3,name="Mac book",description="An IOS device",price=460000,quantity=45),
    Product(id=4,name="Laptop",description="An Windows device",price=235000,quantity=32),
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db=session()

    count=db.query(database_models.Product).count
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()

@app.get("/get_products") #get_products page
def get_products(db:Session=Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/get_products/{id}/") # getting data by using id
def get_products_by_id(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    return "Product Not Found"

@app.post("/product") #adding the product into database(products list)
def add_product(product:Product):
    products.append(product)

@app.put("/product") # Updating the product in the database(products list)
def add_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "Product Updated Successfully"
    return "No such product exists!"

@app.delete("/product") # Removing the product from the db(products list)
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return f"id: {id} product is deleted"
    return f"id: {id} is not present to delete"