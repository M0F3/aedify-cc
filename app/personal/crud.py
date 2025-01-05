from sqlmodel import Session

from app.personal.model import PersonalCreate, Personal


def create_personal(*, session: Session, new_personal_data: PersonalCreate) -> Personal
    new_personal = Personl.model_validate(new_personal_data)
    session.add(new_personal)
    session.commit()
    session.refresh(new_personal)

    return new_personal