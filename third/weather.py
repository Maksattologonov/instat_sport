import asyncio

import aiohttp
import requests
import sys

from decouple import config

sys.path.insert(0, config("BASE_PATH"))
from decouple import config

from third.models import WeatherModel


class GetWeather:
    cities = ["London", "Moscow", "Seattle"]
    api_key = config("API_KEY")

    @classmethod
    async def main(cls):
        for c in cls.cities:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        f"https://api.openweathermap.org/data/2.5/find?q={c}&appid={cls.api_key}") as response:
                    with open("weather_info", "a") as file:
                        data = dict(await response.json())["list"]
                        file.writelines("%s\n" % i for i in data)
                    file.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(GetWeather.main())
