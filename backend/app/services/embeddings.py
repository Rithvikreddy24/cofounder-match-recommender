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
            import importlib
            _http = importlib.import_module("huggingface_hub.utils._http")
            if hasattr(_http, "close_session"):
                getattr(_http, "close_session")()
            elif hasattr(_http, "reset_sessions"):
                getattr(_http, "reset_sessions")()
        except Exception:
            pass

        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
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
    return cast(
        np.ndarray,
        get_model().encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        ),
    )


def generate_embeddings(profiles: list) -> list[np.ndarray]:
    """
    Generate embeddings for all founder profiles.
    """
    return [generate_embedding(profile) for profile in profiles]