from typing import Union
import uvicorn
from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Eine Nachricht": "Hallo Welt!"}

@app.get("/rechnung/{a}-sowie-{b}")
def read_item(a: int, b: int):
    pickle.dump(a, open("saved_number.pck", "wb"))
    return {"Gesendet wurden": str(a) + " und " + str(b) , "Die Summe ist": a+b}

@app.get("/multiplikation/{a}-mal-{b}")
def multiply(a: int, b: int):
    return {"Gesendet wurden": str(a) + " und " + str(b), "Das Produkt ist": a * b}

@app.get("/lade/")
def laden():
    # datei laden
    a = pickle.load(open("saved_number.pck", "rb"))
    return{"Gelesen wurde: ": str(a)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1337)

# ipv4: 127.0.0.1
# 0.0.0.0 ist local host
# standard-port ist 80
# xyz.de aufgerufen -> DNS (Domain-Name-System) aufgerufen -> 126.183.92.23:80

'''commands für 
cd .. -> 1 directory zurück
mkdir -> directory erstellen
ls / cd zeigt alle möglichen Verzeichnisse
'''