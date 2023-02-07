import uvicorn
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


# users api
@app.post("/hs/user/create", response_model=schemas.UserBase)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    crud.create_user(db=db, user=user)


@app.put("/hs/user/change/{id}")
def change_user(id: int, user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(user_id=id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        crud.change_user(db=db, user_id=id, new_user_data=user)


@app.delete("/hs/user/delete/{id}", status_code=200)
def hide_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        crud.hide_user(db=db, user_id=id)
        return {"message": "Помечен на удаление"}


@app.patch("/hs/user/undelete/{id}", status_code=200)
def show_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, user_id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        crud.show_user(db=db, user_id=id)
        return {"message": "Снята пометка на удаление"}


@app.get("/hs/user/list")
def get_users_list(db: Session = Depends(get_db)):
    db_users = crud.get_users(db=db)
    return db_users


@app.get("/hs/user/roleList")
def get_users_role_list(db: Session = Depends(get_db)):
    db_users_role_list = crud.get_users_role_list(db=db)
    return db_users_role_list


@app.post("/hs/user/login")
def log_in(login: str, passwordHash: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db=db, login=login)
    if not db_user or db_user.passwordHash != passwordHash:
        raise HTTPException(status_code=400, detail='Ошибка выполнения, неверный логин или пароль')
    else:
        return crud.get_users(db=db)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8005)

