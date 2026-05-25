from pydantic import BaseModel


class AttendanceResponse(BaseModel):

    person_name: str

    attendance_marked: bool

    timestamp: str