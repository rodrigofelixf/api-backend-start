from functools import lru_cache
import time

@lru_cache(maxsize=100)
def calcula_complexo(numero: int) -> int:
    time.sleep(2)  # Simula uma operação de cálculo demorada
    return numero * numero

# Função para testar o cache
def testar_cache():
    start_time = time.time()
    print(calcula_complexo(4))  # Deve demorar cerca de 2 segundos na primeira chamada
    print("Tempo decorrido (primeira chamada):", time.time() - start_time)

    start_time = time.time()
    print(calcula_complexo(4))  # Deve ser muito mais rápido devido ao cache
    print("Tempo decorrido (segunda chamada):", time.time() - start_time)

# Execute o teste
testar_cache()
