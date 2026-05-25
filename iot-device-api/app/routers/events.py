from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/devices", tags=["Events"])

@router.post("/{device_id}/events", response_model=schemas.EventResponse, status_code=201)
def create_event(device_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    new_event = models.Event(
        device_id=device_id,
        **event.model_dump())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    
    return new_event

@router.get("/{device_id}/events", response_model=List[schemas.EventResponse])
def list_events(device_id: int, db: Session = Depends(get_db)):
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    return device.events