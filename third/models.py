from typing import Optional

from pydantic import BaseModel


class WeatherList(BaseModel):
    name: str


class WeatherMain(BaseModel):
    feels_like: float
    temp_max: float
    rain: Optional[dict]
    snow: Optional[dict]
    clouds: Optional[dict]


class WeatherModel(BaseModel):
    list: WeatherList
    main: WeatherMain
