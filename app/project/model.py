from sqlmodel import SQLModel, Field, Relationship


class ProjectBase(SQLModel):
    name: str

class Project(ProjectBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class ProjectCreate(ProjectBase):
    pass