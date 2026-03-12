from contextlib import asynccontextmanager
from typing import Annotated
import uvicorn
from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session,select
from schemas import Car,CarInput

engine = create_engine("sqlite:///car_sharing.db",echo = True)

@asynccontextmanager
async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title='car sharing app',lifespan=lifespan)

@app.get("/api/cars")
def get_cars(session:Annotated[Session,Depends(get_session)],size:str = None,doors:int=None) ->list:
    query = select(Car)
    if size:
        query = query.where(Car.size>=size)
    if doors:
        query = query.where(Car.doors>=doors)
    return session.exec(query).all()

@app.post("/api/cars")
def post_car(session:Annotated[Session,Depends(get_session)],car_input : CarInput) -> Car:
    new_car = Car.model_validate(car_input)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car

@app.put("/api/cars")
def update_car(session:Annotated[Session,Depends(get_session)],car_input:CarInput,id:int) -> Car:
    car = session.get(Car,id)
    if car:
        car.fuel=car_input.fuel
        car.transmission=car_input.transmission
        car.size=car_input.size
        car.doors=car_input.doors
        session.commit()
        return car
    else:
        raise HTTPException(status_code=404,detail=f"No car is available with provided id={id}")
    

@app.delete("/api/delete-cars/{id}")
def delete_cars(session:Annotated[Session,Depends(get_session)],id:int):
    car=session.get(Car,id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404,detail=f"No car is available with provided id={id}")
    
   #SQLModel is itself an ORM, but it is implemented on top of SQLAlchemy. When we use SQLModel, 
   # we are still using SQLAlchemy under the hood for database connections, sessions, and SQL execution. 
   # We import SQLAlchemy only for core pieces like the engine, while SQLModel simplifies ORM definitions and integrates Pydantic validation for FastAPI.