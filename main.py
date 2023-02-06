from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import crud
from models import schemas, models
from models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/test")
async def pong():
    return {"redfab API": " is works!!"}


# color api
@app.post("/hs/color/create", response_model=schemas.Color)
def create_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_colors(db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)


@app.put("/hs/color/change/{id}", response_model=schemas.Color)
def change_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_colors(db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)


@app.delete("/hs/color/delete/{id}", response_model=schemas.Color)
def delete_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_colors(db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)


@app.patch("/hs/color/undelete/{id}", response_model=schemas.Color)
def undelete_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.set_color(db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)


@app.get("/hs/color/list", response_model=list[schemas.Color])
def get_colors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colors = crud.get_colors(db, skip=skip, limit=limit)
    return colors


@app.post("/hs/color/features/{id}", response_model=schemas.Color)
def create_color(id: int, db: Session = Depends(get_db)):
    db_color = crud.get_features(id=id, db=db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)

