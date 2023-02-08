from datetime import datetime

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from models import crud
from models import schemas, models
from models.database import SessionLocal, engine
import hashlib
from decouple import config
from datetime import datetime, timedelta

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


@app.patch("/hs/color/change/{id}", response_model=schemas.ColorUpdate)
def change_color(id: int, color: schemas.ColorUpdate, db: Session = Depends(get_db)):
    db_color = crud.get_color(db, id=id)
    if not db_color:
        raise HTTPException(status_code=400, detail="Color not found!")
    crud.set_color(db=db, id=id, name=color.name)
    return crud.get_color(db=db, id=id)


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
    return crud.create_user(db=db, user=user)


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
def login(response: Response, login: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db=db, login=login)
    passwordHash = hashlib.md5(str.encode(password, encoding='utf-8')).hexdigest()
    if not db_user or db_user.passwordHash != passwordHash:
        raise HTTPException(status_code=400, detail='Ошибка выполнения, неверный логин или пароль')
    else:
        response.set_cookie(
            key="login",
            value=db_user.login,
            expires=2689200 # 31 days in second + 3 hours(error) = 2689200 sec
        )
        return crud.get_users(db=db, user_id=db_user.id)


@app.post("/hs/user/logout")
def logout(response: Response, login: str | None = Cookie(default=None)):
    if not login:
        return {"message": "Вы не в системе!"}
    else:
        response.delete_cookie(login)
        return {"message": f"{login} вышел из системы"}


@app.get("/hs/user/current")
def get_current_user(login: str | None = Cookie(default=None), db: Session = Depends(get_db)):
    user_db = crud.get_user_by_login(db=db, login=login)
    if not user_db:
        return {"message": "Пользователь не вошел в систему или не существует"}
    else:
        return crud.get_users(db=db, user_id=user_db.id)


@app.get("/hs/user/features/{id}")
def get_features(id: int, db: Session = Depends(get_db)):
    db_features = crud.get_featurs_by_user_id(db=db, user_id=id)
    if not db_features:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        return db_features


# Тест таблиц
@app.get("/test/roles")
def get_roles_list(db: Session = Depends(get_db)):
    return db.query(models.Roles).all()


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8005)

