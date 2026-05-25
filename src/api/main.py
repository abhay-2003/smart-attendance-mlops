from fastapi import FastAPI, UploadFile, File

from src.services.recognition_service import recognize_person
from src.services.attendance_service import fetch_attendance_records
from src.utils.logger import logger


app = FastAPI(
    title="Smart Attendance MLOps API",
    version="2.0"
)


@app.get("/")
def home():

    logger.info("Health check endpoint called")

    return {
        "message": "Smart Attendance API Running"
    }


@app.post("/recognize")
async def recognize_face_api(
    file: UploadFile = File(...)
):

    logger.info("Recognition API called")

    response = recognize_person(file)

    return response


@app.get("/attendance")
def get_attendance():

    logger.info("Attendance API called")

    return fetch_attendance_records()