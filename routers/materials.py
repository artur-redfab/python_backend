from fastapi import APIRouter


router = APIRouter(
    prefix='/hs/material',
    tags=['material']
)


@router.post("/create")
def create_material():
    pass


@router.put("/change/{id}")
def change_material():
    pass


@router.delete("/delete/{id}")
def hide_material():
    pass


@router.patch("/undelete/{id}")
def show_material():
    pass


@router.post("/list")
def get_materials_list():
    pass


@router.get("/features/{id}")
def get_features():
    pass