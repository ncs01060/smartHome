import pymysql,os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()
dbPassword = os.getenv("DB_PASSWORD")
hostName = os.getenv("HOST_NAME")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://smarthome:{dbPassword}@{hostName}:3306/smarthome?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=3600,  
    pool_pre_ping=True,
)

def getDB():
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session()
    

