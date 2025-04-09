from fastapi import FastAPI

app = FastAPI()

# Basic routes:
@app.get("/")
def home():
    return {"message": {"page": "Home!"}}

# install fastapi & uvicorn(pip install fastapi uvicorn)
# import FastAPI
# create a instance of FastAPI
# create a basic route
# run uvicorn ( uvicorn main:app --reload)
