from sqlalchemy.orm import Session
from components.tasks import schemas, models
import hashlib
import os
from components.projects import models as projects_models
from fastapi import UploadFile
from components.taskFiles import models as taskFile_models
from decouple import config


def write_file_data(db: Session, task_id: int,  file_data: UploadFile):
    db_project = db.query(projects_models.Projects).filter(projects_models.Projects.id == models.Tasks.idProject).first()
    path = str(config('FTP_PATH')) + str(file_data.filename)
    name, ext = os.path.splitext(file_data.filename)
    ext = ext.split('.')[1]
    size = (os.stat(path).st_size) / 1048576
    hash = hashlib.md5(open(path, 'rb').read()).hexdigest()
    taskFile = taskFile_models.TaskFiles(
        nameFile=name,
        extFile=ext,
        idTask=task_id,
        idOwner=db_project.idAuthor,
        sizeFile=size,
        hashFile=hash,
        path=path
    )
    db.add(taskFile)
    db.commit()
    db.refresh(taskFile)
    query = db.query(models.Tasks).filter(models.Tasks.id == taskFile.id).first()
    return query.id

