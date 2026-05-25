from fastapi import FastAPI
from .database import engine, Base
from .routers import devices, events

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IoT Device API",
    description="API para gerenciamento de dispositivos de segurança eletrônica",
    version="1.0.0"
)

app.include_router(devices.router)
app.include_router(events.router)

@app.get("/")
def root():
    return {"message": "IoT Device API online 🚀"}