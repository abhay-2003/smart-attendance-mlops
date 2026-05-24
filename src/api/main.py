from fastapi import FastAPI, UploadFile, File
from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import shutil
import os
import pandas as pd

# FASTAPI INITIALIZATION


app = FastAPI(
    title="Smart Attendance MLOps API",
    version="1.0"
)

# CONFIGURATION


EMBEDDINGS_PATH = "data/embeddings/face_embeddings.pkl"

MODEL_NAME = "Facenet"

SIMILARITY_THRESHOLD = 0.82

TEMP_IMAGE_PATH = "temp_api_image.jpg"

# LOAD EMBEDDINGS DATABASE


print("\nLoading embeddings database...")

with open(EMBEDDINGS_PATH, "rb") as file:
    embeddings_database = pickle.load(file)

print("Embeddings loaded successfully!")


# HEALTH CHECK ENDPOINT


@app.get("/")
def home():

    return {
        "message": "Smart Attendance API Running"
    }

# FACE RECOGNITION ENDPOINT


@app.post("/recognize")
async def recognize_face(
    file: UploadFile = File(...)
):

    # SAVE UPLOADED IMAGE
   

    with open(TEMP_IMAGE_PATH, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:

        # GENERATE EMBEDDING
       

        embedding_result = DeepFace.represent(
            img_path=TEMP_IMAGE_PATH,
            model_name=MODEL_NAME,
            enforce_detection=False
        )

        test_embedding = np.array(
            embedding_result[0]["embedding"]
        ).reshape(1, -1)

        # FIND BEST MATCH
     

        best_match_name = None

        best_similarity_score = -1

        for person_name, embeddings_list in embeddings_database.items():

            for stored_embedding in embeddings_list:

                stored_embedding = np.array(
                    stored_embedding
                ).reshape(1, -1)

                similarity = cosine_similarity(
                    test_embedding,
                    stored_embedding
                )[0][0]

                if similarity > best_similarity_score:

                    best_similarity_score = similarity

                    best_match_name = person_name

        # THRESHOLD CHECK
       

        if best_similarity_score >= SIMILARITY_THRESHOLD:

            result = {
                "recognized": True,
                "person": best_match_name,
                "similarity_score": round(
                    float(best_similarity_score),
                    4
                )
            }

        else:

            result = {
                "recognized": False,
                "person": "Unknown",
                "similarity_score": round(
                    float(best_similarity_score),
                    4
                )
            }

    except Exception as error:

        result = {
            "error": str(error)
        }

    # CLEANUP
   

    if os.path.exists(TEMP_IMAGE_PATH):

        os.remove(TEMP_IMAGE_PATH)

    return result

# ATTENDANCE LOG ENDPOINT


@app.get("/attendance")
def get_attendance():

    attendance_path = "data/attendance_logs/attendance.csv"

    if not os.path.exists(attendance_path):

        return {
            "message": "No attendance records found"
        }

    attendance_df = pd.read_csv(
        attendance_path
    )

    return attendance_df.to_dict(
        orient="records"
    )