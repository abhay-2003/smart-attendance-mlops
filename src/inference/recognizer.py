from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pickle

from src.utils.logger import logger
from src.config.settings import settings

from src.services.attendance_service import (
    mark_attendance
)

from src.mlops.mlflow_manager import (
    start_mlflow_run,
    log_recognition_metrics,
    log_recognition_params,
    log_artifacts,
    end_mlflow_run
)


MODEL_NAME = "Facenet"


logger.info(
    "Loading embeddings database..."
)

with open(
    settings.EMBEDDINGS_PATH,
    "rb"
) as file:

    embeddings_database = pickle.load(
        file
    )

logger.info(
    "Embeddings database loaded successfully"
)


def recognize_face(image_path: str):

    try:

        # START MLFLOW RUN

        start_mlflow_run(
            "face_recognition_inference"
        )

        # LOG PARAMETERS

        log_recognition_params(
            MODEL_NAME,
            image_path
        )

        logger.info(
            "Generating embedding for input image"
        )

        embedding_result = DeepFace.represent(
            img_path=image_path,
            model_name=MODEL_NAME,
            enforce_detection=False
        )

        test_embedding = np.array(
            embedding_result[0]["embedding"]
        ).reshape(1, -1)

        logger.info(
            "Embedding generated successfully"
        )

        best_match_name = None

        best_similarity_score = -1

        logger.info(
            "Comparing embeddings"
        )

        for person_name, embeddings_list in (
            embeddings_database.items()
        ):

            for stored_embedding in (
                embeddings_list
            ):

                stored_embedding = np.array(
                    stored_embedding
                ).reshape(1, -1)

                similarity = cosine_similarity(
                    test_embedding,
                    stored_embedding
                )[0][0]

                if similarity > (
                    best_similarity_score
                ):

                    best_similarity_score = (
                        similarity
                    )

                    best_match_name = (
                        person_name
                    )

        logger.info(
            "Face comparison completed"
        )

        confidence_percentage = round(
            best_similarity_score * 100,
            2
        )

        # THRESHOLD CHECK

        if (
            best_similarity_score
            >= settings.SIMILARITY_THRESHOLD
        ):

            status = "MATCH FOUND"

            mark_attendance(
                best_match_name
            )

        else:

            best_match_name = "Unknown"

            status = "UNKNOWN PERSON"

        logger.info(
            f"Recognition Status: {status}"
        )

        # LOG MLFLOW METRICS

        log_recognition_metrics(
            similarity_score=
                float(best_similarity_score),

            threshold=
                settings.SIMILARITY_THRESHOLD,

            recognized=
                (
                    status
                    ==
                    "MATCH FOUND"
                )
        )

        # LOG ARTIFACTS

        log_artifacts()

        # END MLFLOW RUN

        end_mlflow_run()

        return {

            "predicted_person":
                best_match_name,

            "similarity_score":
                round(
                    float(
                        best_similarity_score
                    ),
                    4
                ),

            "confidence_percentage":
                confidence_percentage,

            "status":
                status
        }

    except Exception as error:

        end_mlflow_run()

        logger.error(
            f"Recognition Error: {error}"
        )

        return {

            "predicted_person":
                None,

            "similarity_score":
                0.0,

            "confidence_percentage":
                0.0,

            "status":
                "ERROR",

            "error":
                str(error)
        }


if __name__ == "__main__":

    result = recognize_face(
        "test.jpg"
    )

    print(
        "\nRECOGNITION RESULT\n"
    )

    print(result)