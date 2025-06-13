from pydantic import BaseModel, constr
from typing import List

class ResponseModel(BaseModel):
    windowPrevState: List[int]
    windowCurrstate: List[int]
    numbers: List[int]
    avg: float    