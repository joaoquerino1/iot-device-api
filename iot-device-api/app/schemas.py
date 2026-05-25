from pydantic import BaseModel 
from datetime import datetime
from typing import Optional

# --- Device ---
class DeviceCreate(BaseModel):
    name : str
    type : str
    location : Optional[str] = None

class DeviceResponse(BaseModel):
    id : int
    name : str
    type : str
    location : Optional[str] 
    is_active : bool
    created_at : datetime

    class Config:
        from_attributes = True

# --- Event ---
class EventCreate(BaseModel):
    type : str
    description : Optional[str] = None

class EventResponse(BaseModel):
    id : int
    device_id : int
    type : str
    description : Optional[str]
    occurred_at : datetime

    class Config:
        from_attributes = True
