from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.db import get_db
from models.data import WindowState
from database.schemas import ResponseModel
from fetcher import fetch_numbers

router = APIRouter()
WINDOW_SIZE = 10

@router.get("/numbers/{numbers_id}", response_model=ResponseModel)
async def get_numbers(numbers_id: int, db: AsyncSession = Depends(get_db)):
    if numbers_id not in ['p','f','e','r']:
        raise HTTPException(status_code=404, detail="Invalid numbers_id")
    result = await db.execute(select(windowstate).where(windowState.number.id == numbers_id))
    output = result.scalars_one_or_none()
    
    prev = state.numbers if state else []
    new_numbers = await fetch_numbers(number_id)
    
    filtered = [n for n in new_numbers if n not in prev]
    
    cur = (prev + filtered)[:WINDOW_SIZE]
    if len(curr) > WINDOW_SIZE:
        curr = curr[-WINDOW_SIZE:]

    avg = round(sum(cur) / len(curr), 2) if cur else 0.0
    
    if state:
        state.numbers = cur
        state.average = avg
    else:
        state = WindowState(number_id = number_id, numbers=curr)
        db.add(state)
        
    await db.commit()
    
    return {
        windowPrevState: prev, 
        windowCurrstate: cur,
        numbers: filtered,
        avg: avg
    }
        