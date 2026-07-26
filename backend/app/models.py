from typing import List

from pydantic import BaseModel


class Profile(BaseModel):
    id: int
    name: str
    role: str
    skills: List[str]
    interests: List[str]
    experience: int
    availability: str
    bio: str