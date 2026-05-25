from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/devices", tags=["devices"])

@router.post("/", response_model=schemas.DeviceResponse, status_code=201)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    new_device = models.Device(**device.model_dump())
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

@router.get("/", response_model=List[schemas.DeviceResponse])
def list_devices(db: Session = Depends(get_db)):
    return db.query(models.Device).all()

@router.get("/{device_id}", response_model=schemas.DeviceResponse)
def get_device(device_id: int, db: Session = Depends(get_db)):
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    return device

@router.patch("/{device_id}/toggle", response_model=schemas.DeviceResponse)
def toggle_device(device_id: int, db: Session = Depends(get_db)):
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    device.is_active = not device.is_active
    db.commit()
    db.refresh(device)
    return device

