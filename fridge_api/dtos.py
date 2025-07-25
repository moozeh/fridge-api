
from pydantic import BaseModel, Field
from typing import List, Literal

class RecipeRequest(BaseModel):
    ingredients: List[str]