from fastapi import FastAPI
from routes.production import router as ProductionRouter

app = FastAPI()
app.include_router(ProductionRouter, tags=["Production"], prefix="/production")


@app.get("/")
async def welcome():
    return {"message": "Welcome  to this fantastic app"}
