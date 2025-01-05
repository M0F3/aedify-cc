from sqlmodel import SQLModel, Field


class ProjectBase(SQLModel):
    name: str


class Project(ProjectBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class ProjectPublic(ProjectBase):
    id: int

class ProjectCreate(ProjectBase):
    pass