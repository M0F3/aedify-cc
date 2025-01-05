from sqlmodel import SQLModel, Field


class PersonalBase(SQLModel):
    first_name: str
    last_name: str


class Personal(PersonalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PersonalCreate(PersonalBase):
    pass
