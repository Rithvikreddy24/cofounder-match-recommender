from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.matching import get_recommendations, profiles_dict

app = FastAPI(
    title="Co-founder Match Recommender API",
    description="Backend API for recommending co-founder matches using embeddings and weighted matching logic.",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Co-founder Match Recommender API. Visit /docs for documentation."}

@app.get("/api/matches/{user_id}")
def read_matches(user_id: int):
    # Validate user exists
    if user_id not in profiles_dict:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
        
    try:
        recommendations = get_recommendations(user_id)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating matches: {str(e)}")
