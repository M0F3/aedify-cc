from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from app.assignment.crud import update_assignment, create_assignment
from app.assignment.model import Assignment, AssignmentUpdate
from app.database.database import get_database

router = APIRouter(prefix="/assignments", tags=["assignments"])

@router.get("", response_model=list[Assignment])
def list_assignments(*, session: Session = Depends(get_database)):
    return session.exec(select(Assignment))

@router.post("", response_model=Assignment, status_code=status.HTTP_201_CREATED)
def add_assignment(*, session: Session = Depends(get_database), new_assignment_data: Assignment):
    return create_assignment(session=Session, new_assignment_data=new_assignment_data)

@router.put("/{assignment_id}", response_model=Assignment)
def update_assignment(*, session: Session = Depends(get_database), assignment_id: int, update_assignment_data: AssignmentUpdate):
    return update_assignment(session=Session, assignment_id=assignment_id, updated_assignment_data=update_assignment_data)