import uvicorn
from fastapi import FastAPI
from models import models
from models.database import engine
from routers.color import router as color_routers
from routers.user import router as user_routers
from routers.materials import router as materials_routers
from routers.polymerbases import router as polymerBases_routers

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/test")
async def pong():
    return {"redfab API": " is works!!"}


# color api
app.include_router(color_routers)
# users api
app.include_router(user_routers)
# polymerBases api
app.include_router(polymerBases_routers)

# materials api
app.include_router(materials_routers)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8005)

