from configparser import ConfigParser
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.clusters import crud, schemas
from db.database import get_db

# instantiate
configP = ConfigParser()
# parse existing file
configP.read('messages.ini')

cluster_router = APIRouter(
    prefix='/hs/cluster',
    tags=['cluster']
)


@cluster_router.post('/create', response_model=schemas.CreateChangeCluster)
def create(base: schemas.CreateChangeCluster, db: Session = Depends(get_db)):
    return crud.create_cluster(cluster=base, db=db)


@cluster_router.put('/change/{id}', status_code=200)
def change(id: int, base: schemas.CreateChangeCluster, db: Session = Depends(get_db)):
    crud.change_cluster(cluster_id=id, new_cluster=base, db=db)
    return JSONResponse(status_code=200, content=configP.get('clusters', 'cluster_changed_success'))


@cluster_router.delete('/delete/{id}', status_code=200)
def hide(id: int, db: Session = Depends(get_db)):
    crud.hide_cluster(cluster_id=id, db=db)
    return JSONResponse(status_code=200, content=configP.get('clusters', 'cluster_deleted'))


@cluster_router.patch('/undelete/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db)):
    crud.show_cluster(cluster_id=id, db=db)
    return JSONResponse(status_code=200, content=configP.get('clusters', 'cluster_undeleted'))


@cluster_router.get('/list', response_model=list[schemas.Cluster])
def get_clusters_list(db: Session = Depends(get_db)):
    return crud.get_clusters(db=db)


@cluster_router.get('/features/{id}', response_model=schemas.FeaturesCluster)
def get_features(id: int, db: Session = Depends(get_db)):
    return crud.get_features(cluster_id=id, db=db)


@cluster_router.get('/all', response_model=list[schemas.AllDataClusters])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_info(db=db)
# протестить с опергрупс

