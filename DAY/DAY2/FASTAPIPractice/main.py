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