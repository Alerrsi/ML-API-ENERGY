from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}


Base.metadata.create_all(bind=engine)  # creates tables if they don't exist

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user