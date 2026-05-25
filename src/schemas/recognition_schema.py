from pydantic import BaseModel


class RecognitionResponse(BaseModel):

    predicted_person: str

    similarity_score: float

    status: str
    