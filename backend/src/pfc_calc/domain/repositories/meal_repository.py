from abc import ABC, abstractmethod

from pfc_calc.domain.entities.meal import Meal


class MealRepository(ABC):
    @abstractmethod
    def list_meals(self) -> list[Meal]:
        raise NotImplementedError
