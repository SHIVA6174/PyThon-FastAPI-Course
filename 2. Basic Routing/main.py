from fastapi import FastAPI

app = FastAPI()


# Basic routes:
@app.get("/")
def home():
    return {"message": {"page": "Home!"}}


@app.get("/about")
def about():
    return {"message": {"page": "About!"}}


@app.get("/user")
def getUser():
    return {"data": {"name": "Shiva WebDev", "email": "shiva@gmail.com"}}

