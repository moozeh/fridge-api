
from pydantic import BaseModel
from typing import List

class IngredientItem(BaseModel):
    name: str