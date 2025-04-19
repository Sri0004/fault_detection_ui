from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL (using SQLite for now, can be changed to PostgreSQL or MySQL if needed)
DATABASE_URL = "sqlite:///./fault_detection.db"

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for ORM models
Base = declarative_base()

# Function to initialize the database
def init_db():
    import app.models  # Import models before creating tables
    Base.metadata.create_all(bind=engine)
