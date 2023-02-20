import uvicorn
from fastapi import FastAPI
from components.vacuumSystem import models
from db.database import engine
from components.colors.routers import router as colors_routers
from components.users.routers import router as user_routers
from components.materials.routers import router as materials_routers
from components.projects.routers import router as projects_routers
from components.vacuumSystem.routers import router as vacuumSystem_routers
from components.polymerBases.routers import router as polymerBases_routers
from components.makers.routers import router as makers_routers

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/test")
async def pong():
    return {"redfab API": " is works!!"}


# color api
app.include_router(colors_routers)
# users api
app.include_router(user_routers)
# project api
app.include_router(projects_routers)
# vacuumSystem api
app.include_router(vacuumSystem_routers)
# polymerBases api
app.include_router(polymerBases_routers)
# materials api
app.include_router(materials_routers)
# makers api
app.include_router(makers_routers)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8005)

