from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id:int
    username:str
    password:str
    created_at: datetime
