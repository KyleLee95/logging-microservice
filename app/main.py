from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.logging_service.routes import router as log_router
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.include_router(log_router, prefix="/logs")


@app.on_event("startup")
async def startup_event():
    print("Starting up the favorites service...")


@app.get("/")
async def root():
    return {"message": "Welcome to the Logging Microservice"}


@app.exception_handler(StarletteHTTPException)
async def not_found_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "Sorry, we couldn't find that!"},
        )

    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})
