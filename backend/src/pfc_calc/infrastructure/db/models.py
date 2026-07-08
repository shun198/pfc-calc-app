from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from pfc_calc.infrastructure.db.base import Base


class MealModel(Base):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    protein_grams: Mapped[int] = mapped_column(Integer)
    fat_grams: Mapped[int] = mapped_column(Integer)
    carb_grams: Mapped[int] = mapped_column(Integer)
    eaten_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
