from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle

# CONFIGURATION


EMBEDDINGS_PATH = "data/embeddings/face_embeddings.pkl"

TEST_IMAGE_PATH = "test.jpg"

MODEL_NAME = "Facenet"


# LOAD STORED EMBEDDINGS


print("\nLoading embeddings database...")

with open(EMBEDDINGS_PATH, "rb") as file:
    embeddings_database = pickle.load(file)

print("Embeddings loaded successfully!")


# GENERATE EMBEDDING FOR TEST IMAGE


print("\nGenerating embedding for test image...")

test_embedding_result = DeepFace.represent(
    img_path=TEST_IMAGE_PATH,
    model_name=MODEL_NAME,
    enforce_detection=False
)

test_embedding = np.array(
    test_embedding_result[0]["embedding"]
).reshape(1, -1)

print("Test embedding generated!")

# FIND BEST MATCH


best_match_name = None
best_similarity_score = -1

print("\nComparing with stored embeddings...\n")

for person_name, embeddings_list in embeddings_database.items():

    for stored_embedding in embeddings_list:

        stored_embedding = np.array(
            stored_embedding
        ).reshape(1, -1)

       
        # CALCULATE COSINE SIMILARITY
       

        similarity = cosine_similarity(
            test_embedding,
            stored_embedding
        )[0][0]

       
        # UPDATE BEST MATCH
       

        if similarity > best_similarity_score:

            best_similarity_score = similarity
            best_match_name = person_name

# FINAL RESULT



print("RECOGNITION RESULT")


print(f"Predicted Person: {best_match_name}")

print(f"Similarity Score: {best_similarity_score:.4f}")


# THRESHOLD CHECK


THRESHOLD = 0.70

if best_similarity_score >= THRESHOLD:

    print("\nMATCH FOUND!")

else:

    print("\nUNKNOWN PERSON!")