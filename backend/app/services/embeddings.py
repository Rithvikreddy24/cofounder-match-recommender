from typing import cast
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def profile_to_text(profile: dict) -> str:
    """
    Convert a founder profile into a single text string for embedding.
    """
    return (
        f"Role: {profile['role']}. "
        f"Skills: {', '.join(profile['skills'])}. "
        f"Interests: {', '.join(profile['interests'])}. "
        f"Bio: {profile['bio']}"
    )


def generate_embedding(profile: dict) -> np.ndarray:
    """
    Generate an embedding for a single founder profile.
    """
    text = profile_to_text(profile)
    return cast(np.ndarray, model.encode(text))


def generate_embeddings(profiles: list) -> list[np.ndarray]:
    """
    Generate embeddings for all founder profiles.
    """
    return [generate_embedding(profile) for profile in profiles]