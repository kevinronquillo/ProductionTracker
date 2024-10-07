# main.py
from fastapi import FastAPI
from server.database import init_db
from routes.Production import router as ProductionRouter
from routes.ProductionCategory import router as ProductionCategoryRouter
from routes.Payout import router as PayoutRouter
from routes.User import router as UserRouter
from routes.Login import router as LoginRouter

app = FastAPI()

# Initialize Beanie and MongoDB
@app.on_event("startup")
async def on_startup():
    await init_db()

# Include the production router
#TODO Add SoftDelete and Timestamp to these models
app.include_router(ProductionRouter, tags=["Production"], prefix="/Production")
app.include_router(ProductionCategoryRouter, tags=["Production Category"],prefix="/ProductionCategory")
app.include_router(PayoutRouter, tags=["Payout"], prefix="/Payout")
app.include_router(UserRouter, tags=["User"], prefix="/User")
app.include_router(LoginRouter, tags=["Login"], prefix="/Login")
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Production API!"}