from fastapi import APIRouter, Depends

from app.presentation.api.dependencies import get_list_meals_usecase
from app.presentation.api.schemas import MealResponse
from app.usecases.list_meals import ListMealsUseCase

router = APIRouter()


@router.get("/meals", response_model=list[MealResponse])
def list_meals(
    usecase: ListMealsUseCase = Depends(get_list_meals_usecase),
) -> list[MealResponse]:
    meals = usecase.execute()
    return [MealResponse.from_entity(meal) for meal in meals]
