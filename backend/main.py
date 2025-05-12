from fastapi import FastAPI
from backend.routers import casino  # auth rimosso per ora

app = FastAPI(title="Casino Online API", version="1.0")

app.include_router(casino.router)

@app.get("/")
def root():
    return {"message": "Benvenuto nel Casinò Online"}
