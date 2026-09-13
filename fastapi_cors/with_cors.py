from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],   # кому разрешаем
    allow_credentials=True,                     # можно ли слать куки/токены
    allow_methods=["*"],                        # какие методы разрешаем
    allow_headers=["*"],                        # какие заголовки разрешаем
)


@app.get("/api/hello")
def hello():
    print("[FASTAPI-CORS:5002] Получен GET /api/hello")
    return {"message": "Привет с сервера С CORS (FastAPI)!", "port": 5002}


if __name__ == "__main__":
    print("FastAPI-сервер С CORS запущен на http://localhost:5002")
    uvicorn.run(app, host="localhost", port=5002)





  #             Origin
  #               |
  #   ____________|_________
  #   |           |        |
  #   |           |        |
  # Protocol    Domain    Port
  #   |           |        |
  #   |           |        |
  # http/https://127.0.0.1:8000/


