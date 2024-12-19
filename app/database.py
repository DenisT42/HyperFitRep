from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# # Load environment variables (optional, if you store credentials in .env)
# from dotenv import load_dotenv
# load_dotenv()

# Database connection URL (replace with your actual connection details)
DATABASE_URL = "mysql+asyncmy://root:hyperfit11@localhost:3401/hyperfit_DB"  # Default to SQLite if not set

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





# DATABASE_URL = "mysql+asyncmy://root:kwarteng@localhost:3401/Hyperfit"
#
# engine = create_async_engine(DATABASE_URL,echo = True)