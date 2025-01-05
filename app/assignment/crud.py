from fastapi import HTTPException, status
from sqlmodel import Session

from app.assignment.model import Assignment, AVAILABLE_ASSIGNMENT_STATUS, AVAILABLE_ASSIGNMENT_ROLES, AssignmentUpdate
from app.personal.model import Personal


def create_assignment(*, session: Session, new_assignment_data: Assignment) -> Assignment:
    new_assignment = Assignment.model_validate(new_assignment_data)
    validate_assignment_data(new_assignment_data.model_dump(exclude_unset=True))
    session.add(new_assignment)
    session.commit()
    session.refresh(new_assignment)

    return new_assignment

def update_assignment(*, session: Session, data: AssignmentUpdate, assignment_id: int) -> Assignment:
    db_assignment = get_assignment(session=session, assignment_id=assignment_id)
    updated_assignment = data.model_dump(exclude_unset=True)
    validate_assignment_data(updated_assignment)

    if "personal_id" in updated_assignment.keys():
        if not session.get(Personal, updated_assignment["personal_id"]):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Personal does not exist")

    for key, value in updated_assignment.items():
        setattr(db_assignment, key, value)

    session.add(db_assignment)
    session.commit()
    session.refresh(db_assignment)
    return db_assignment


def validate_assignment_data(assignment_data: dict):
    if "status" in assignment_data.keys():
        if assignment_data["status"] not in AVAILABLE_ASSIGNMENT_STATUS:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid status given")
        # TODO validate other things which should be validated for a state transition

    if "role" in assignment_data.keys() and assignment_data["role"] not in AVAILABLE_ASSIGNMENT_ROLES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role does not exist")


def get_assignment(*, session: Session, assignment_id: int) -> Assignment:
    db_assignment = session.get(Assignment, assignment_id)
    if not db_assignment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Assignment does not exist")
    return db_assignment
