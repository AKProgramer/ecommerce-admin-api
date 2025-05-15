from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Set database credentials directly
DB_USERNAME = "root"  # Set your DB username here
DB_PASSWORD = "1234"  # Set your DB password here
DB_HOST = "localhost"      # Set your DB host here
DB_NAME = "ecommerce_db"   # Set your DB name here

if not DB_USERNAME or not DB_PASSWORD or not DB_HOST or not DB_NAME:
    raise EnvironmentError("Database username, password, host, and name must be set in this file (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME).")

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()