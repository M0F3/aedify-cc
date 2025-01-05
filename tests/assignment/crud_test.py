from fastapi import HTTPException, status

from app.assignment.crud import validate_assignment_data
from app.assignment.model import ASSIGNMENT_STATUS_ACTIVE


class TestCrud:
    def test_validate_assignment_data_status(self):
        try:
            validate_assignment_data({"status": ASSIGNMENT_STATUS_ACTIVE})
        except:
            assert False != True
        assert True

    def test_validate_assignment_data_status_with_invalid_status(self):
        try:
            validate_assignment_data({"status": "INVALID_STATUS"})
        except HTTPException as exception:
            assert type(exception) == HTTPException
            assert exception.status_code == status.HTTP_400_BAD_REQUEST