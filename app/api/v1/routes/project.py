from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database.database import get_database
from app.project.model import Project, ProjectCreate

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=Project)
def create_project(*, session: Session = Depends(get_database), new_project_data: ProjectCreate):
    new_project = Project.model_validate(new_project_data)
    session.add(new_project)
    session.commit()
    session.refresh(new_project)

    return new_project