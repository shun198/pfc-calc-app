from fastapi import APIRouter, Depends, status

from pfc_calc.presentation.api.dependencies import get_list_meals_usecase
from pfc_calc.presentation.api.schemas import MealResponse
from pfc_calc.usecases.list_meals import ListMealsUseCase

router = APIRouter()


@router.get(
    "/meals",
    response_model=list[MealResponse],
    status_code=status.HTTP_200_OK,
)
def list_meals(
    usecase: ListMealsUseCase = Depends(get_list_meals_usecase),
) -> list[MealResponse]:
    meals = usecase.execute()
    return [MealResponse.from_entity(meal) for meal in meals]
