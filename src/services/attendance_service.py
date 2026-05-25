import os
import pandas as pd
from datetime import datetime

from src.utils.logger import logger


ATTENDANCE_PATH = (
    "data/attendance_logs/attendance.csv"
)


def mark_attendance(person_name: str):

    os.makedirs(
        "data/attendance_logs",
        exist_ok=True
    )

    current_time = datetime.now()

    attendance_record = {

        "person_name": person_name,

        "date": current_time.strftime(
            "%Y-%m-%d"
        ),

        "time": current_time.strftime(
            "%H:%M:%S"
        )
    }

    # CREATE FILE IF NOT EXISTS

    if not os.path.exists(
        ATTENDANCE_PATH
    ):

        attendance_df = pd.DataFrame(
            [attendance_record]
        )

        attendance_df.to_csv(
            ATTENDANCE_PATH,
            index=False
        )

        logger.info(
            f"Attendance created for {person_name}"
        )

        return

    attendance_df = pd.read_csv(
        ATTENDANCE_PATH
    )

    # DUPLICATE PREVENTION

    today = current_time.strftime(
        "%Y-%m-%d"
    )

    already_marked = attendance_df[
        (attendance_df["person_name"] == person_name)
        &
        (attendance_df["date"] == today)
    ]

    if len(already_marked) > 0:

        logger.info(
            f"Attendance already marked for {person_name}"
        )

        return

    updated_df = pd.concat(
        [
            attendance_df,
            pd.DataFrame([attendance_record])
        ],
        ignore_index=True
    )

    updated_df.to_csv(
        ATTENDANCE_PATH,
        index=False
    )

    logger.info(
        f"Attendance marked for {person_name}"
    )


def fetch_attendance_records():

    if not os.path.exists(
        ATTENDANCE_PATH
    ):

        return {
            "message": (
                "No attendance records found"
            )
        }

    attendance_df = pd.read_csv(
        ATTENDANCE_PATH
    )

    return attendance_df.to_dict(
        orient="records"
    )