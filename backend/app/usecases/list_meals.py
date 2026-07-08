from app.domain.entities.meal import Meal
from app.domain.repositories.meal_repository import MealRepository


class ListMealsUseCase:
    def __init__(self, meal_repository: MealRepository) -> None:
        self.meal_repository = meal_repository

    def execute(self) -> list[Meal]:
        return self.meal_repository.list_meals()
