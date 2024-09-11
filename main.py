from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis.asyncio import Redis
from contextlib import asynccontextmanager
from app.api.routes import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializa o Redis e o cache
    redis = Redis(host="localhost", port=6379, db=0)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    # Transição para o estado de operação
    yield

    # Finaliza o Redis
    await redis.close()

# Cria a instância do FastAPI com o lifespan
app = FastAPI(lifespan=lifespan)

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens; ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos; ajuste conforme necessário
    allow_headers=["*"],  # Permite todos os cabeçalhos; ajuste conforme necessário
)

# Inclui o roteador da API
app.include_router(api_router, prefix="/v1/api")
