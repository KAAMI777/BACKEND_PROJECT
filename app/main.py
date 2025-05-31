from fastapi import FastAPI,Depends,HTTPException,status,APIRouter
import routers.user as user
from MODELS.db_conn import engine
import MODELS.db_conn as modelss
# from MODELS.db_conn import models, engine


app = FastAPI()
modelss.Base.metadata.create_all(bind=engine)
print("it is connected")

app.include_router(user.router)