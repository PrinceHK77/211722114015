from fastapi import FastAPI 
from models import data
from database import schemas
from database.db import engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(data.Base.metadata.create_all)
        
        
