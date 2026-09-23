from fastapi import FastAPI
from app.config import settings
from app.database import ping_database
#creating fastapi instance
app = FastAPI(title=settings.APP_NAME)
#this function runs once when the application starts up, it checks if the database is reachable and raises an error if not. It also prints a message indicating that the connection to MongoDB was successful.
@app.on_event("startup")
def on_startup():
    if not ping_database():
        raise RuntimeError("could not connect to MongoDB")
    print(f"[startup]Connected to MongoDB. App: {settings.APP_NAME}")
#checks basic health-check of API endpoint and confirms GET/ is running and reachable.
@app.get("/",tags=["Health"])
def health_check():
    return {"status": "ok", "app_name": settings.APP_NAME}