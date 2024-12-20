from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Async database URL (replace with your database credentials)
DATABASE_URL = "mysql+asyncmy://root:hyperfit11@localhost:3401/hyperfit_DB"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a sessionmaker for async sessions
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base class for defining ORM models
Base = declarative_base()

# Dependency to provide async database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session









