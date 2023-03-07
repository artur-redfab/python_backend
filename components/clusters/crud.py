from fastapi import HTTPException
from sqlalchemy.orm import Session
from components.clusters import schemas, models
from components.stands import models as stands_models
from components.makers.routers import configP


def get_cluster_by_id(cluster_id: int, db: Session):
    cluster = db.query(models.Clusters).filter(models.Clusters.id == cluster_id).first()
    return cluster


def create_cluster(cluster: schemas.CreateChangeCluster, db: Session):
    cluster = models.Clusters(name=cluster.name)
    db.add(cluster)
    db.commit()
    db.refresh(cluster)
    return cluster


def change_cluster(cluster_id: int, new_cluster: schemas.CreateChangeCluster, db: Session):
    cluster = get_cluster_by_id(cluster_id=cluster_id, db=db)
    if not cluster:
        raise HTTPException(status_code=404, detail=configP.get('clusters', 'cluster_not_found'))
    else:
        cluster.name = new_cluster.name
        db.commit()


def hide_cluster(cluster_id: int, db: Session):
    cluster = get_cluster_by_id(cluster_id=cluster_id, db=db)
    if not cluster:
        raise HTTPException(status_code=404, detail=configP.get('clusters', 'cluster_not_found'))
    else:
        cluster.markingDeletion = True
        db.commit()


def show_cluster(cluster_id: int, db: Session):
    cluster = get_cluster_by_id(cluster_id=cluster_id, db=db)
    if not cluster:
        raise HTTPException(status_code=404, detail=configP.get('clusters', 'cluster_not_found'))
    else:
        cluster.markingDeletion = False
        db.commit()


def get_clusters(db: Session):
    clusters = db.query(models.Clusters).all()
    return clusters


def get_features(cluster_id: int, db: Session):
    cluster = get_cluster_by_id(cluster_id=cluster_id, db=db)
    if not cluster:
        raise HTTPException(status_code=404, detail=configP.get('clusters', 'cluster_not_found'))
    else:
        return cluster


def get_all_info(db: Session):
    clusters = db.query(models.Clusters).all()
    return clusters

