import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite engine
DATABASE_URL = "sqlite:///./questions.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    import app.models  # Import the models to ensure they are registered with SQLAlchemy
    Base.metadata.drop_all(bind=engine)  # Drop all tables
    Base.metadata.create_all(bind=engine) # Create all tables
    

    db = SessionLocal()

    # Create users with plain text passwords if they don't already exist
    users = [
        {"username": "alice", "password": "wonderland"},
        {"username": "bob", "password": "builder"},
        {"username": "clementine", "password": "mandarine"},
        {"username": "admin", "password": "4dm1N"},
    ]

    for user in users:
         db_user = db.query(app.models.User).filter(app.models.User.username == user["username"]).first()
         if not db_user:
            db_user = app.models.User(username=user["username"], password=user["password"])
            db.add(db_user)

    db.commit()
    db.close()
# Load data from Excel and store it in the database
def load_data():
    df = pd.read_excel('data/questions_en.xlsx')
    df.to_sql('questions', engine, if_exists='replace', index=False)