from typing import cast, Optional
import numpy as np
from sentence_transformers import SentenceTransformer

# Lazy load the model
model: Optional[SentenceTransformer] = None


def get_model() -> SentenceTransformer:
    global model
    if model is None:
        # Clear any stale closed client inside huggingface_hub (crucial for Windows/Uvicorn reloads)
        try:
            from huggingface_hub.utils._http import close_session
            close_session()
        except ImportError:
            pass

        # Try loading locally from cache first to avoid network queries and httpx reload bugs
        try:
            model = SentenceTransformer("all-MiniLM-L6-v2", local_files_only=True)
        except Exception:
            # Fallback to online loading if model is not yet cached
            model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


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
    return cast(np.ndarray, get_model().encode(text))


def generate_embeddings(profiles: list) -> list[np.ndarray]:
    """
    Generate embeddings for all founder profiles.
    """
    return [generate_embedding(profile) for profile in profiles]