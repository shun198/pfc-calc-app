from datetime import datetime, timezone

from app.domain.entities.meal import Meal
from app.domain.repositories.meal_repository import MealRepository


class StubMealRepository(MealRepository):
    def list_meals(self) -> list[Meal]:
        now = datetime.now(timezone.utc)
        return [
            Meal(
                id=1,
                name="Breakfast bowl",
                protein_grams=30,
                fat_grams=11,
                carb_grams=45,
                eaten_at=now,
            ),
            Meal(
                id=2,
                name="Chicken lunch",
                protein_grams=42,
                fat_grams=13,
                carb_grams=58,
                eaten_at=now,
            ),
        ]
