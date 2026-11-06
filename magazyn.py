import uvicorn
from fastapi import FastAPI

app = FastAPI()

towary = {"klawiatura": 5, "mysz": 10, "monitor": 2}


@app.get("/stan")
def stan():
    return towary


uvicorn.run(app, host="127.0.0.1", port=8001)