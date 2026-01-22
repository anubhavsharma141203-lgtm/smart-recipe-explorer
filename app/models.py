from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=200)
    ingredients: List[str] = Field(..., min_items=1)
    instructions: str = Field(..., min_length=10)
    cuisine: str = Field(..., min_length=1)
    servings: Optional[int] = 4
    prep_time: Optional[int] = None  # in minutes
    cook_time: Optional[int] = None  # in minutes

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Spaghetti Carbonara",
                "ingredients": ["pasta", "eggs", "bacon", "cheese"],
                "instructions": "Cook pasta, mix with bacon and eggs",
                "cuisine": "Italian",
                "servings": 4,
                "prep_time": 10,
                "cook_time": 20
            }
        }

class RecipeResponse(Recipe):
    id: int

class AIResponse(BaseModel):
    suggestion: str
    ingredients_used: List[str]

class SearchFilters(BaseModel):
    cuisine: Optional[str] = None
    ingredient: Optional[str] = None
    prep_time_max: Optional[int] = None
