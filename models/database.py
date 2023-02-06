from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import PostgresDsn
from decouple import config


SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme="postgresql",
    user=config('PG_USER'),
    password=config('PG_PASS'),
    host=config('PG_SERVER'),
    port=config('PG_PORT'),
    path=f"/{config('PG_DB') or ''}",
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
try:
    db = SessionLocal()
    db.execute("SELECT 1")
except Exception as e:
    raise e

Base = declarative_base()
