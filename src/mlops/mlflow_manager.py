import os
import mlflow

from datetime import datetime

from src.config.settings import settings
from src.utils.logger import logger


EXPERIMENT_NAME = (
    "Smart_Attendance_MLOps"
)


mlflow.set_tracking_uri(
    settings.MLFLOW_TRACKING_URI
)

mlflow.set_experiment(
    EXPERIMENT_NAME
)


def start_mlflow_run(
    run_name: str
):

    logger.info(
        f"Starting MLflow run: {run_name}"
    )

    return mlflow.start_run(
        run_name=run_name
    )


def log_recognition_metrics(
    similarity_score: float,
    threshold: float,
    recognized: bool
):

    mlflow.log_metric(
        "similarity_score",
        similarity_score
    )

    mlflow.log_metric(
        "threshold",
        threshold
    )

    mlflow.log_metric(
        "recognized",
        int(recognized)
    )


def log_recognition_params(
    model_name: str,
    image_path: str
):

    mlflow.log_param(
        "model_name",
        model_name
    )

    mlflow.log_param(
        "image_path",
        image_path
    )

    mlflow.log_param(
        "timestamp",
        str(datetime.now())
    )


def log_artifacts():

    artifact_paths = [

        "data/attendance_logs/attendance.csv",

        "logs/app.log"
    ]

    for artifact_path in artifact_paths:

        if os.path.exists(
            artifact_path
        ):

            mlflow.log_artifact(
                artifact_path
            )

            logger.info(
                f"Artifact logged: {artifact_path}"
            )


def end_mlflow_run():

    logger.info(
        "Ending MLflow run"
    )

    mlflow.end_run()