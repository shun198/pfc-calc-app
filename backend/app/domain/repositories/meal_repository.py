from abc import ABC, abstractmethod

from app.domain.entities.meal import Meal


class MealRepository(ABC):
    @abstractmethod
    def list_meals(self) -> list[Meal]:
        raise NotImplementedError
