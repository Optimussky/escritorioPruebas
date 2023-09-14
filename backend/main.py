# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
from schemas import UserData, UserId
from models import Base


#Con la instrucción Base.metadata.create_all(bind=engine) se van a crear las tablas si
# no están creadas, y de estar creadas no sufren cambios.
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return 'Prueba desde el index en FastAPI'

@app.get('/api/users/', response_model=list[UserId])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)
"""
Levantar el servidor desde terminal:
     uvicorn main:app --host 0.0.0.0 --port 8900 --reload
"""
