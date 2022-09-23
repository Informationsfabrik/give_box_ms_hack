from database import SessionLocal

# Helper function to access DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
