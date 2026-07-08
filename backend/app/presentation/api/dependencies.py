from app.infrastructure.repositories.stub_meal_repository import StubMealRepository
from app.usecases.list_meals import ListMealsUseCase


def get_list_meals_usecase() -> ListMealsUseCase:
    repository = StubMealRepository()
    return ListMealsUseCase(meal_repository=repository)
