import os
import shutil

from src.inference.recognizer import (
    recognize_face
)

from src.utils.logger import logger


TEMP_IMAGE_PATH = (
    "temp_api_image.jpg"
)


def recognize_person(uploaded_file):

    logger.info(
        "Saving uploaded image"
    )

    with open(
        TEMP_IMAGE_PATH,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            uploaded_file.file,
            buffer
        )

    try:

        result = recognize_face(
            TEMP_IMAGE_PATH
        )

        logger.info(
            "Recognition service completed"
        )

        return result

    finally:

        if os.path.exists(
            TEMP_IMAGE_PATH
        ):

            os.remove(
                TEMP_IMAGE_PATH
            )

            logger.info(
                "Temporary image removed"
            )