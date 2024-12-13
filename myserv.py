from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Eine Nachricht": "Hallo Welt!"}


@app.get("/rechnung/{a}-sowie-{b}")
def read_item(a: int, b: int):
    return {"Gesendet wurden": str(a) + " und " + str(b) , "Die Summe ist": a+b}

#if __name__ == "__main__":
#    uvicorn.run(app, host="192.168.0.1", port=1337)
# ipv4: 127.0.0.1
# 0.0.0.0 ist local host
# standard-port ist 80
# xyz.de aufgerufen -> DNS (Domain-Name-System) aufgerufen -> 126.183.92.23:80