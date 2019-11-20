#!/usr/bin/python3

from envirophat import weather
from envirophat import motion
from envirophat import light
import json
import requests
import os

if __name__ == "__main__":
    url = os.environ["ENDPOINT"]
    print(url)

    sensorsJson = json.dumps({
        "temperature": weather.temperature(),
        "pressure": weather.pressure(unit="hPa"),
        "light": light.light(),
        "rgb": light.rgb(),
    }, sort_keys=True, indent=2)

    print("------")
    print(sensorsJson)

    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=sensorsJson, headers=headers)
