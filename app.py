from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from routes.state import router as StateRouter
from routes.city import router as CityRouter
from routes.admin import router as AdminRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(StateRouter, tags=["States"], prefix="/states", dependencies=[Depends(token_listener)])
app.include_router(CityRouter, tags=["Cities"], prefix="/cities", dependencies=[Depends(token_listener)])