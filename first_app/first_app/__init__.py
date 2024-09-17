from dataclasses import dataclass
from typing import Union
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi import FastAPI

app = FastAPI()

config = Config()
config.bind = [
    "localhost:8080",
    "localhost:8000",
]


@dataclass
class Vasya:
    name: str
    age: int


@app.get("/", response_model=Vasya)
async def read_root():
    # return NotImplementedError("Deprecated")
    return {"name": "Vaselisa", "age": 2024 - 1997}


@app.get(
    "/items/{item_id}",
)
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def main():
    asyncio.run(serve(app, config))
