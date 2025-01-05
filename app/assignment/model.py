from typing import Final

from pydantic.v1 import NoneStr
from sqlmodel import SQLModel, Field, Relationship
from app.project.model import Project
from app.personal.model import Personal

ASSIGNMENT_STATUS_ACTIVE: Final[str] = "Active"
ASSIGNMENT_STATUS_COMPLETED: Final[str] = "Completed"
ASSIGNMENT_STATUS_CANCELED: Final[str] = "Canceled"

AVAILABLE_ASSIGNMENT_STATUS = [
    ASSIGNMENT_STATUS_ACTIVE,
    ASSIGNMENT_STATUS_CANCELED,
    ASSIGNMENT_STATUS_COMPLETED
]

ASSIGNMENT_ROLE_FOREMAN: Final[str] = "Foreman"
ASSIGNMENT_ROLE_LABORER: Final[str] = "Laborer"

AVAILABLE_ASSIGNMENT_ROLES = [
    ASSIGNMENT_ROLE_LABORER,
    ASSIGNMENT_ROLE_FOREMAN
]

class AssignmentBase(SQLModel):
    role: str
    start_time: int
    end_time: int | None
    status: str
    project_id: int = Field(foreign_key="project.id")
    personal_id: int | None = Field(default=None, foreign_key="personal.id")

class Assignment(AssignmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class AssignmentUpdate(SQLModel):
    role: str | None = None
    start_time: int | None = None
    end_time: int | None = None
    status: str  | None = None
    project_id: int | None = None
    personal_id: int | None = None
