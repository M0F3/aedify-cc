from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database.database import get_database
from app.personal.crud import create_personal
from app.personal.model import Personal, PersonalCreate

router = APIRouter(prefix="/personals", tags=["personals"])

@router.post("/", response_model=Personal)
def add_personal(*, session: Session = Depends(get_database), new_personal_data: PersonalCreate):
    return create_personal(session=session, new_personal_data=new_personal_data)
