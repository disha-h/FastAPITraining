from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "HelloWorld","number":44,"is_fun":True}