from sqlalchemy.orm import sessionmaker # Creates database session objects
from sqlalchemy import create_engine    # Creates a connection engine to the database
from sqlalchemy.ext.declarative import declarative_base  # Base class for ORM models
import os

# Get the DATABASE_URL from environment variables. 
# Database connection URL (PostgreSQL)
# Format: postgresql://username:password@host:port/database
# If not found, fallback to your local connection string (useful for local testing).
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:1323@localhost:5432/harshith")

# Fix for Render's postgres URL: Render uses "postgres://", but SQLAlchemy requires "postgresql://"
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(db_url) # Engine handles the actual connection to the database
session = sessionmaker(
    autocommit=False,   # Changes must be committed manually
    autoflush=False,    # Prevents automatic DB writes
    bind=engine         # Binds session to the engine
) # session is used to talk to the database (CRUD operations)
Base = declarative_base()  # Base class used to define database tables as Python classes