from pydantic import BaseModel


class SolarPanel(BaseModel):
    # Class  fields
    model: str
    output_power: float
