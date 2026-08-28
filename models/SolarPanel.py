from pydantic import BaseModel
from main import app

class SolarPanel(BaseModel):
    # Class  fields
    model: str
    output_power: float
    state: float


    @app.get("api/solarpanel")
    def
