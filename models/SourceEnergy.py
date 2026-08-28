from typing import Literal

from pydantic import BaseModel, Field

from main import app


class SourceEnergy(BaseModel):
    # Class  fields
    model: str = Field(min_length=2, max_length=50)
    output_power: float = Field()
    description: str = Field(max_length=100)
    type: Literal[0, 1, 2]
    state: bool
