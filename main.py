import json

from fastapi import FastAPI

from models import Brand, Snowboard


with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

app = FastAPI()

snowboards: list[Snowboard] = []

for snowboard in snowboard_list:
    snowboards.append(Snowboard(**snowboard))

@app.get("/snowboards")
async def get_snowboard() -> list[Snowboard]:
    return snowboards

@app.post("/snowboards")
async def add_snowboard(snowboard: Snowboard) -> None:
    snowboards.append(snowboard)

@app.put("/snowboards/{id}")
async def update_snowboard(id: int, updated_snowboard: Snowboard) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == id:
            snowboards[i] = updated_snowboard
            return
    snowboards.append(updated_snowboard)

@app.delete("/snowboards/{id}")
async def delete_snowboard(id: int) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == id:
            snowboards.pop(i)
            return