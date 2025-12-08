from typing import Union
from fastapi import FastAPI
from datetime import datetime
import zoneinfo

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/time/{iso_code}")
async def get_time(iso_code: str):
  # Co => CO
  iso = iso_code.upper()
  timezone_str = country_timezones.get(iso)

  if not timezone_str:
    return {"error": f"Country code '{iso}' not supported"}

  tz = zoneinfo.ZoneInfo(timezone_str)
  return {"time": datetime.now(tz)}
