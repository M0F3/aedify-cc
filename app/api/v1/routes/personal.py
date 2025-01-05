from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database.database import get_database
from app.personal.model import Personal, PersonalCreate

router = APIRouter(prefix="/personals", tags=["personals"])

@router.post("/", response_model=Personal)
def create_personal(*, session: Session = Depends(get_database), new_personal_data: PersonalCreate):
    new_personal = Personal.model_validate(new_personal_data)
    session.add(new_personal)
    session.commit()
    session.refresh(new_personal)

    return new_personal
