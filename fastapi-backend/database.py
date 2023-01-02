from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


def get_sqlalchemy_url() -> str:
    user = getenv("POSTGRES_USER", "postgres")
    password = getenv("POSTGRES_PASSWORD")
    host = getenv("POSTGRES_HOST", "postgres")
    port = getenv("POSTGRES_PORT", 5432)
    db = getenv("POSTGRES_DB", "postgres")
    print(f"postgresql+psycopg2://{user}:******@{host}:{port}/{db}")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"


engine = create_engine(get_sqlalchemy_url(), pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
