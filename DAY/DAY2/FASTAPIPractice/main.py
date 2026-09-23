from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"page": "home"}
@app.get("/about")
def about():
    return {"page": "about","author": "John Doe"}

@app.get("/health")
def health():
    return {"status": "ok"}
#POST request
@app.post("/create")
def create_something():
    return {"message": "something created"}
#path parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"result":"Distinction","usn":usn}
#path parameters with type hint
@app.get("/candidate/{rollno}")
def get_candidate(rollno:int):
    return {"result":"Distinction","rollno":rollno}
#pydantic model
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock:bool=True
@app.post("/items")
def create_item(item: Item):
    return {"received": item,"total_price": item.price * 1.18} #adding tax
