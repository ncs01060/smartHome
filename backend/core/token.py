import jwt,os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

tokenMinute = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")) # type: ignore
key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

def createAcessToken(data:dict):
    encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=tokenMinute)
    encode.update({"exp":expire})

    encode_jwt = jwt.encode(encode, key, algorithm=algorithm )
    return encode_jwt
