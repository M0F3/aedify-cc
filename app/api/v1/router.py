from fastapi import APIRouter

from app.api.v1.routes import assignment
from app.api.v1.routes import personal
from app.api.v1.routes import project

router = APIRouter(prefix="/v1")

router.include_router(assignment.router)
router.include_router(personal.router)
router.include_router(project.router)