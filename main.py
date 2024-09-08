from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI()

# Incluir o roteador
app.include_router(api_router, prefix="/v1/api")
