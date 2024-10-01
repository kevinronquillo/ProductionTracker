# main.py
from fastapi import FastAPI
from server.database import init_db
from routes.production import router as ProductionRouter

app = FastAPI()

# Initialize Beanie and MongoDB
@app.on_event("startup")
async def on_startup():
    await init_db()

# Include the production router
app.include_router(ProductionRouter, tags=["Production"], prefix="/production")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Production API!"}
