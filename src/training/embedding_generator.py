from deepface import DeepFace
import os
import pickle
from tqdm import tqdm


# CONFIGURATION


# Dataset path
DATASET_PATH = "data/raw/lfw-deepfunneled"

# Output embeddings file
EMBEDDINGS_OUTPUT_PATH = "data/embeddings/face_embeddings.pkl"

# DeepFace model configuration
MODEL_NAME = "Facenet"


# CREATE EMBEDDINGS DIRECTORY IF NOT EXISTS


os.makedirs("data/embeddings", exist_ok=True)


# EMBEDDINGS STORAGE DICTIONARY


embeddings_database = {}

# START PROCESS


print("\n====================================")
print("FACE EMBEDDING GENERATION STARTED")
print("====================================\n")


# ITERATE THROUGH EACH PERSON FOLDER


person_folders = os.listdir(DATASET_PATH)

for person_name in tqdm(person_folders, desc="Processing Persons"):

    person_path = os.path.join(DATASET_PATH, person_name)

    # Skip non-folder files
    if not os.path.isdir(person_path):
        continue

    # Initialize person's embedding list
    embeddings_database[person_name] = []

    # ITERATE THROUGH PERSON IMAGES
    

    image_files = os.listdir(person_path)

    for image_name in image_files:

        image_path = os.path.join(person_path, image_name)

        try:

            # GENERATE FACE EMBEDDING
           

            embedding_result = DeepFace.represent(
                img_path=image_path,
                model_name=MODEL_NAME,
                enforce_detection=False
            )

            
            # EXTRACT EMBEDDING VECTOR
            

            embedding_vector = embedding_result[0]["embedding"]

            
            # STORE EMBEDDING
           

            embeddings_database[person_name].append(
                embedding_vector
            )

        except Exception as error:

            print(f"\nError processing image: {image_path}")
            print(error)


# SAVE EMBEDDINGS DATABASE


with open(EMBEDDINGS_OUTPUT_PATH, "wb") as file:

    pickle.dump(embeddings_database, file)


# COMPLETION MESSAGE



print("EMBEDDINGS GENERATED SUCCESSFULLY")


print(f"\nEmbeddings saved at:")
print(EMBEDDINGS_OUTPUT_PATH)

print("\nTotal Persons Processed:")
print(len(embeddings_database))