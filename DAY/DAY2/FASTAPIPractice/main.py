from fastapi import FastAPI
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
