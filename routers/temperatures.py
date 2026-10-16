from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.database import get_db
import crud

router = APIRouter(tags=["temperature"])
DBDep = Annotated[AsyncSession, Depends(get_db)]


@router.get("/temperatures", response_model=list[schemas.TemperatureResponse])
async def get_temperatures(db: DBDep):
    return await crud.get_temperatures(db)

@router.get("/temperatures/", response_model=list[schemas.TemperatureResponse])
async def get_temperature_by_city_id(city_id: int, db: DBDep):
    return await crud.get_temperature_by_city_id(db, city_id)

@router.post("/temperatures/update", response_model=schemas.TemperatureResponse, status_code=status.HTTP_201_CREATED)
async def add_temperature(data: schemas.TemperatureCreate, db: DBDep):
    try:
        return await crud.add_temperature(db, data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
