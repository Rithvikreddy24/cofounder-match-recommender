import os
import json
import numpy as np
from typing import List, Dict, Any
from app.services.embeddings import generate_embedding, generate_embeddings

# Define base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_PATH = os.path.join(BASE_DIR, "data", "profiles.json")

# Helper to load profiles
def load_profiles() -> List[Dict[str, Any]]:
    with open(PROFILES_PATH, "r") as f:
        return json.load(f)

# Load profiles
profiles = load_profiles()
profiles_dict = {p["id"]: p for p in profiles}
profile_embeddings = {}

def initialize_embeddings():
    """
    Precompute and cache embeddings for all profiles.
    """
    global profile_embeddings
    embeddings = generate_embeddings(profiles)
    for p, emb in zip(profiles, embeddings):
        profile_embeddings[p["id"]] = emb


def compute_cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Compute the cosine similarity between two numpy vectors.
    """
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    return float(dot_product / (norm_vec1 * norm_vec2))

def get_skill_overlap(skills1: List[str], skills2: List[str]) -> float:
    """
    Calculate normalized skill overlap using the overlap coefficient.
    Ratio is intersection divided by the minimum size of the two sets.
    """
    set1 = set(s.lower().strip() for s in skills1)
    set2 = set(s.lower().strip() for s in skills2)
    if not set1 or not set2:
        return 0.0
    intersection = set1.intersection(set2)
    return len(intersection) / min(len(set1), len(set2))

def get_interest_overlap(interests1: List[str], interests2: List[str]) -> float:
    """
    Calculate Jaccard similarity for interest overlap.
    """
    set1 = set(i.lower().strip() for i in interests1)
    set2 = set(i.lower().strip() for i in interests2)
    if not set1 or not set2:
        return 0.0
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

def get_role_complementarity(role1: str, role2: str) -> float:
    """
    Determine role complementarity score based on startup roles.
    Tech + Biz = 1.0
    Tech + Design = 0.9
    Biz + Design = 0.8
    Tech + Tech (different roles) = 0.6
    Biz + Biz (different roles) = 0.4
    Identical roles = 0.3
    """
    r1 = role1.strip()
    r2 = role2.strip()
    
    if r1 == r2:
        return 0.3
        
    tech_roles = {
        "AI Engineer", "Machine Learning Engineer", "Full Stack Developer", 
        "Backend Developer", "Frontend Developer", "Mobile Developer", 
        "Data Scientist", "DevOps Engineer", "Cybersecurity Engineer", "Cloud Engineer"
    }
    biz_roles = {"Product Manager", "Business Development", "Marketing Strategist", "Sales Lead"}
    design_roles = {"UI/UX Designer"}
    
    def get_group(r: str) -> str:
        if r in tech_roles:
            return "TECH"
        if r in biz_roles:
            return "BIZ"
        if r in design_roles:
            return "DESIGN"
        return "OTHER"
        
    g1 = get_group(r1)
    g2 = get_group(r2)
    
    if (g1 == "TECH" and g2 == "BIZ") or (g2 == "TECH" and g1 == "BIZ"):
        return 1.0
    if (g1 == "TECH" and g2 == "DESIGN") or (g2 == "TECH" and g1 == "DESIGN"):
        return 0.9
    if (g1 == "BIZ" and g2 == "DESIGN") or (g2 == "BIZ" and g1 == "DESIGN"):
        return 0.8
    if g1 == "TECH" and g2 == "TECH":
        return 0.6
    if g1 == "BIZ" and g2 == "BIZ":
        return 0.4
        
    return 0.5

def get_availability_compatibility(avail1: str, avail2: str) -> float:
    """
    Score compatibility of time availability.
    Full match = 1.0
    Full-time + Part-time = 0.7
    Part-time + Weekends = 0.5
    Full-time + Weekends = 0.3
    """
    a1 = avail1.strip()
    a2 = avail2.strip()
    if a1 == a2:
        return 1.0
        
    pair = {a1, a2}
    if pair == {"Full-time", "Part-time"}:
        return 0.7
    if pair == {"Part-time", "Weekends"}:
        return 0.5
    if pair == {"Full-time", "Weekends"}:
        return 0.3
        
    return 0.4

def get_recommendations(user_id: int, top_n: int = 5) -> List[Dict[str, Any]]:
    """
    Generate top N recommendations for a query user ID.
    Excludes the queried user, computes a weighted score, sorts by score desc.
    """
    # Lazy initialize embeddings if not already cached
    if not profile_embeddings:
        initialize_embeddings()

    if user_id not in profiles_dict:
        raise ValueError(f"Profile with ID {user_id} does not exist.")
        
    user_profile = profiles_dict[user_id]
    user_emb = profile_embeddings[user_id]
    
    scored_candidates = []
    
    for candidate in profiles:
        if candidate["id"] == user_id:
            continue
            
        candidate_id = candidate["id"]
        candidate_emb = profile_embeddings[candidate_id]
        
        # 1. Semantic Similarity
        semantic_sim = compute_cosine_similarity(user_emb, candidate_emb)
        
        # 2. Skill Overlap
        skill_overlap = get_skill_overlap(user_profile["skills"], candidate["skills"])
        
        # 3. Interest Overlap
        interest_overlap = get_interest_overlap(user_profile["interests"], candidate["interests"])
        
        # 4. Role Complementarity
        role_comp = get_role_complementarity(user_profile["role"], candidate["role"])
        
        # 5. Availability Compatibility
        avail_comp = get_availability_compatibility(user_profile["availability"], candidate["availability"])
        
        # Weighted Scoring Formula
        match_score = (
            0.4 * semantic_sim +
            0.2 * skill_overlap +
            0.15 * interest_overlap +
            0.15 * role_comp +
            0.1 * avail_comp
        )
        
        # Create recommendation copy and inject match score
        rec = dict(candidate)
        rec["match_score"] = round(match_score, 4)
        scored_candidates.append(rec)
        
    # Sort descending by match_score
    scored_candidates.sort(key=lambda x: x["match_score"], reverse=True)
    
    return scored_candidates[:top_n]
