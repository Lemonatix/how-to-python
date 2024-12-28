from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message: Hello World."}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully!", "item": item}

# To run the server, open a terminal and type:
# uvicorn fastapi_example:app --reload

# Then visit http://127.0.0.1:8000/docs to see the automatically generated Swagger UI.