from fastapi import APIRouter,HTTPException, Depends,status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from core.token import createAcessToken
from core.database import getDB
from models.user import User
import bcrypt
from sqlalchemy import select

router = APIRouter(prefix="/auth", tags=["auth"])

class Rogin(BaseModel):
    username:str
    password:str

@router.post("/login")
def login(req:Rogin,db: Session = Depends(getDB)):
    
    stmt = select(User).where(User.username == req.username) # type: ignore
    user = db.scalars(stmt).first()

    if not user or not bcrypt.checkpw(req.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="아이디 또는 비밀번호가 올바르지 않습니다.",
    )

    access_token = createAcessToken(data={"sub": user.username})
    return {
      "access_token": access_token,
      "token_type": "bearer",
      "username": user.username,
    }
    
