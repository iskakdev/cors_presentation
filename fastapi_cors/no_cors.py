from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/api/hello")
def hello():
    print("[FASTAPI-NO-CORS:5001] Получен GET /api/hello")
    return {"message": "Привет с сервера БЕЗ CORS (FastAPI)!", "port": 5001}


if __name__ == "__main__":
    print("FastAPI-сервер БЕЗ CORS запущен на http://localhost:5001")
    uvicorn.run(app, host="localhost", port=5001)
