from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

# Valores permitidos para o tipo de dispositivo
DEVICE_TYPES = ["camera", "sensor", "alarm"]

# Valores permitidos para o tipo de evento
EVENT_TYPES = ["motion", "alarm_triggered", "offline", "online"]


# --- Device ---

# Schema usado ao CRIAR um dispositivo (dados que chegam na requisição)
class DeviceCreate(BaseModel):
    name: str
    type: str
    location: Optional[str] = None  # Campo opcional

    # Validador que roda automaticamente ao receber o campo "type"
    @field_validator("type")
    @classmethod
    def validate_device_type(cls, v):
        if v not in DEVICE_TYPES:
            # Se o valor não for válido, lança um erro com mensagem clara
            raise ValueError(f"Tipo inválido. Use: {DEVICE_TYPES}")
        return v  # Se válido, retorna o valor normalmente


# Schema usado ao RETORNAR um dispositivo (dados que saem na resposta)
class DeviceResponse(BaseModel):
    id: int
    name: str
    type: str
    location: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        # Permite que o Pydantic leia dados diretamente do modelo SQLAlchemy
        from_attributes = True


# --- Event ---

# Schema usado ao CRIAR um evento
class EventCreate(BaseModel):
    type: str
    description: Optional[str] = None  # Descrição é opcional

    # Validador que roda automaticamente ao receber o campo "type"
    @field_validator("type")
    @classmethod
    def validate_event_type(cls, v):
        if v not in EVENT_TYPES:
            # Se o valor não for válido, lança um erro com mensagem clara
            raise ValueError(f"Tipo inválido. Use: {EVENT_TYPES}")
        return v  # Se válido, retorna o valor normalmente


# Schema usado ao RETORNAR um evento
class EventResponse(BaseModel):
    id: int
    device_id: int
    type: str
    description: Optional[str]
    occurred_at: datetime

    class Config:
        # Permite que o Pydantic leia dados diretamente do modelo SQLAlchemy
        from_attributes = True