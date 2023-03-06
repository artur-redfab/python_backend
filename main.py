import uvicorn
from fastapi import FastAPI
from components.vacuumSystem import models
from db.database import engine
# from components.colors.routers import router as colors_routers
from components.users.routers import router as user_routers
from components.materials.routers import router as materials_routers
from components.projects.routers import router as projects_routers
from components.vacuumSystem.routers import router as vacuumSystem_routers
from components.polymerBases.routers import router as polymerBases_routers
from components.makers.routers import router as makers_routers
from components.tasks.routers import router as tasks_routers
from components.printers.routers import router as printers_routers
from components.sensors.routers import router as sensors_routers
from components.partners.routers import router as partners_routers
from components.nozzles.routersTypes import router as nozzletypes_routers
from components.nozzles.routersSizes import router as nozzlesizes_routers
from components.packing.routers import router as packing_routers
from components.clusters.routers import cluster_router

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/test")
async def pong():
    return {"redfab API": " is works!!"}


# color api
# app.include_router(colors_routers)
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
# tasks api
app.include_router(tasks_routers)
# printers api
app.include_router(printers_routers)
# sensors api
app.include_router(sensors_routers)
# partners api
app.include_router(partners_routers)
# nozzleTypes api
app.include_router(nozzletypes_routers)
# nozzleSizes api
app.include_router(nozzlesizes_routers)
# packing api
app.include_router(packing_routers)
# clusters api
app.include_router(cluster_router)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8005)

