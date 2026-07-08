from datetime import datetime

from pydantic import BaseModel

from app.domain.entities.meal import Meal


class MealResponse(BaseModel):
    id: int
    name: str
    protein_grams: int
    fat_grams: int
    carb_grams: int
    eaten_at: datetime

    @classmethod
    def from_entity(cls, meal: Meal) -> "MealResponse":
        return cls(
            id=meal.id,
            name=meal.name,
            protein_grams=meal.protein_grams,
            fat_grams=meal.fat_grams,
            carb_grams=meal.carb_grams,
            eaten_at=meal.eaten_at,
        )
