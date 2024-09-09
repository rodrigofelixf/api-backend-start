from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router

app = FastAPI()

# Incluir o roteador
app.include_router(api_router, prefix="/v1/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens; ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos; ajuste conforme necessário
    allow_headers=["*"],  # Permite todos os cabeçalhos; ajuste conforme necessário
)

