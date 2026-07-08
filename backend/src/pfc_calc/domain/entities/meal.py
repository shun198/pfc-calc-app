from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Meal:
    id: int
    name: str
    protein_grams: int
    fat_grams: int
    carb_grams: int
    eaten_at: datetime
