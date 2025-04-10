from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()


# Basic routes:
@app.get("/")
def home():
    return {"message": {"page": "Home!"}}


@app.get("/about")
def about():
    return {"message": {"page": "About!"}}


# path parameters


@app.get("/api/user/{id}")
def user(id: int):
    return {"userId": id}


# QUery Parameters: http://127.0.0.1:8000/api/video?videoId=4881&title=fastapi


@app.get("/api/video")
def queryParams(videoId: int, title):
    return {"message": {"videoID": videoId, "videoTitle": title}}


# Req.body
class Products(BaseModel):
    pID: int
    pName: str
    pCost: str
    pAvailable: bool
    pBrand: Optional[str]


@app.post("/api/products")
def Products(requset: Products):
    print(f"PId: {requset.pID} pName: {requset.pName}")
    return {"Product": requset}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=6174)
