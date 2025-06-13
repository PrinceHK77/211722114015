from sqlalchemy import JSON, Column, Integer, String, DateTime
from database.db import Base
import datetime 

class WindowState(Base):
    __tablename__= "window_state"
    id = Column(Integer, primary_key = True, index = True)
    number = Column(String, index = True)
    numbers = Column(JSON)
    
    