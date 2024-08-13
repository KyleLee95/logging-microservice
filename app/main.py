from fastapi import FastAPI
from logging_service.routes import router as log_router

app = FastAPI()

app.include_router(log_router, prefix="/logs")


@app.get("/")
async def root():
    return {"message": "Welcome to the Logging Microservice"}
