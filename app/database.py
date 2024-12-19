from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Async database URL (replace with your database credentials)
DATABASE_URL = "mysql+asyncmy://root:hyperfit11@localhost:3401/hyperfit_DB"

# Create the asynchronous SQLAlchemy engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True  # Logs all SQL statements (useful for debugging; turn off in production)
)

# Create an asynchronous session maker
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # Keeps objects "alive" after session commit
)

# Base class for defining ORM models
Base = declarative_base()

# Dependency to get the async database session
async def get_db():
    """
    Yields a database session for use in FastAPI routes.
    Ensures the session is properly closed after use.
    """
    async with AsyncSessionLocal() as session:
        yield session