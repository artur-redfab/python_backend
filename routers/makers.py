from fastapi import APIRouter


router = APIRouter(
    prefix='/hs/makers',
    tags=['makers']
)


@router.post("/create")
def create_maker():
    pass


@router.put("/change/{id}")
def change_maker():
    pass


@router.delete("/delete/{id}")
def hide_maker():
    pass


@router.patch("/undelete/{id}")
def show_maker():
    pass


@router.get("/list")
def get_makers_list():
    pass


@router.get("/features/{id}")
def get_features():
    pass

