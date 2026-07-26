import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.matching import get_recommendations, profiles_dict

client = TestClient(app)

def test_matching_logic_exclude_self():
    user_id = 1
    recommendations = get_recommendations(user_id)
    # Check top 5 returned
    assert len(recommendations) == 5
    # Check queried user is excluded
    recommended_ids = [r["id"] for r in recommendations]
    assert user_id not in recommended_ids

def test_matching_logic_ordering():
    user_id = 1
    recommendations = get_recommendations(user_id)
    # Check descending order of match_score
    scores = [r["match_score"] for r in recommendations]
    assert scores == sorted(scores, reverse=True)

def test_api_endpoint_valid_user():
    response = client.get("/api/matches/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    for profile in data:
        assert "id" in profile
        assert "name" in profile
        assert "match_score" in profile

def test_api_endpoint_invalid_user():
    response = client.get("/api/matches/9999")
    assert response.status_code == 404
    assert "detail" in response.json()
