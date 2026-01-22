from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change this to ["*"] to allow all connections initially
    allow_methods=["*"],
    allow_headers=["*"],
)
database_models.Base.metadata.create_all(bind=engine)

@app.get("/") #home page
def greet():
    return {
        "message": "Hello Everyone, Welcome to My FastAPI Project!",
        "instructions": "Go to /docs to see the Swagger UI and test the API."
    }

products=[
    Product(id=1,name="Iphone",description="An IOS device",price=150000,quantity=3),
    Product(id=2,name="Samsung",description="An Android device",price=75000,quantity=4),
    Product(id=3,name="Mac book",description="An IOS device",price=460000,quantity=45),
    Product(id=4,name="Laptop",description="An Windows device",price=235000,quantity=32),
]

# ---------- DATABASE SESSION ----------
def get_db():
    db = session()              # Create database session
    try:
        yield db                # Provide session to API routes
    finally:
        db.close()              # Close session after request


# ---------- INITIAL DATABASE DATA ----------
def init_db():
    db = session()              # Create database session
    count = db.query(database_models.Product).count() # Count number of products in table
    if count == 0:              # If table is empty
        for product in products:
            db.add(database_models.Product(**product.model_dump()))  # Insert product data
        db.commit()             # Save changes to database

init_db()                       # Run DB initialization at startup


# ---------- API ROUTES ----------
@app.get("/products")       # Get all products
def get_products(db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).all() # Fetch all products
    return db_product



@app.get("/products/{id}/") # Get product by ID
def get_products_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() # Fetch product with given ID
    if db_product:
        return db_product          # Return product if found
    return "Product Not Found"  # If product does not exist



@app.post("/products") #adding the product into database(products list)
def add_product(product:Product, db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit() # Save changes to database
    return product



@app.put("/products") # Updating the product in the database(products list)
def add_product(id:int, product:Product, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return product
    else:
        return f"No Product found with id: {id}"



@app.delete("/products") # Removing the product from the db(products list)
def delete_product(id:int, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return f"id: {id} is deleted"
    return f"id: {id} is not present to delete"