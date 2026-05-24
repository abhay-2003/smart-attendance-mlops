from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import cv2
import pandas as pd
from datetime import datetime
import os


# CONFIGURATION


EMBEDDINGS_PATH = "data/embeddings/face_embeddings.pkl"

ATTENDANCE_LOG_PATH = "data/attendance_logs/attendance.csv"

MODEL_NAME = "Facenet"

# Better threshold for large dataset
SIMILARITY_THRESHOLD = 0.82

# LOAD EMBEDDINGS DATABASE


print("\nLoading embeddings database...")

with open(EMBEDDINGS_PATH, "rb") as file:
    embeddings_database = pickle.load(file)

print("Embeddings loaded successfully!")


# CREATE ATTENDANCE FILE IF NOT EXISTS


if not os.path.exists(ATTENDANCE_LOG_PATH):

    attendance_df = pd.DataFrame(
        columns=["Name", "Date", "Time"]
    )

    attendance_df.to_csv(
        ATTENDANCE_LOG_PATH,
        index=False
    )

# FUNCTION TO MARK ATTENDANCE


def mark_attendance(name):

    current_time = datetime.now()

    date_string = current_time.strftime("%Y-%m-%d")

    time_string = current_time.strftime("%H:%M:%S")

    attendance_df = pd.read_csv(
        ATTENDANCE_LOG_PATH
    )

    # Prevent duplicate attendance
    already_marked = (
        (attendance_df["Name"] == name) &
        (attendance_df["Date"] == date_string)
    ).any()

    if already_marked:

        print(f"{name} attendance already marked today.")

        return

    new_record = pd.DataFrame({
        "Name": [name],
        "Date": [date_string],
        "Time": [time_string]
    })

    attendance_df = pd.concat(
        [attendance_df, new_record],
        ignore_index=True
    )

    attendance_df.to_csv(
        ATTENDANCE_LOG_PATH,
        index=False
    )

    print(f"Attendance marked for {name}")


# START WEBCAM


print("\nStarting webcam...")

camera = cv2.VideoCapture(0)


# FRAME SKIPPING FOR PERFORMANCE


frame_counter = 0


# REAL-TIME LOOP


while True:

    success, frame = camera.read()

    if not success:

        print("Failed to capture frame.")

        break

   
    # FRAME SKIPPING OPTIMIZATION
   

    frame_counter += 1

    # Process only every 30th frame
    if frame_counter % 30 != 0:

        cv2.imshow(
            "Smart Attendance System",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

        continue

    # SAVE CURRENT FRAME TEMPORARILY
    

    temp_image_path = "temp_frame.jpg"

    cv2.imwrite(temp_image_path, frame)

    label = "Unknown"

    try:

       
        # GENERATE EMBEDDING
       

        embedding_result = DeepFace.represent(
            img_path=temp_image_path,
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

                
                # UPDATE BEST MATCH
               

                if similarity > best_similarity_score:

                    best_similarity_score = similarity

                    best_match_name = person_name

    
        # RECOGNITION RESULT
       

        if best_similarity_score >= SIMILARITY_THRESHOLD:

            label = f"{best_match_name} ({best_similarity_score:.2f})"

            mark_attendance(best_match_name)

        else:

            label = "Unknown"

    except Exception as error:

        print(error)

  
    # DISPLAY RESULT
   

    cv2.putText(
        frame,
        label,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # SHOW WEBCAM WINDOW
   

    cv2.imshow(
        "Smart Attendance System",
        frame
    )

    # PRESS Q TO EXIT


    if cv2.waitKey(1) & 0xFF == ord('q'):

        break


# CLEANUP


camera.release()

cv2.destroyAllWindows()

if os.path.exists("temp_frame.jpg"):

    os.remove("temp_frame.jpg")

print("\nAttendance system stopped.")