from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SSL_CA_PATH = os.getenv("MYSQL_SSL_CA")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is missing. Add it to .env or your deployment environment variables.")

connect_args = {}
if SSL_CA_PATH:
    connect_args["ssl"] = {"ca": SSL_CA_PATH}

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args=connect_args
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()




