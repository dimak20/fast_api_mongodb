from __future__ import annotations

from pydantic import BaseModel, Field


class Location(BaseModel):
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str


class Condition(BaseModel):
    text: str
    icon: str
    code: int


class AirQuality(BaseModel):
    co: float
    no2: float
    o3: float
    so2: float
    pm2_5: float
    pm10: float
    us_epa_index: int = Field(..., alias='us-epa-index')
    gb_defra_index: int = Field(..., alias='gb-defra-index')


class Current(BaseModel):
    last_updated_epoch: int
    last_updated: str
    temp_c: int
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: int
    pressure_in: float
    precip_mm: float
    precip_in: int
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    vis_km: int
    vis_miles: int
    uv: int
    gust_mph: float
    gust_kph: float
    air_quality: AirQuality


class WeatherModel(BaseModel):
    location: Location
    current: Current

data = {
  "location": {
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom",
    "lat": 51.52,
    "lon": -0.11,
    "tz_id": "Europe/London",
    "localtime_epoch": 1613896955,
    "localtime": "2021-02-21 8:42"
  },
  "current": {
    "last_updated_epoch": 1613896210,
    "last_updated": "2021-02-21 08:30",
    "temp_c": 11,
    "temp_f": 51.8,
    "is_day": 1,
    "condition": {
      "text": "Partly cloudy",
      "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
      "code": 1003
    },
    "wind_mph": 3.8,
    "wind_kph": 6.1,
    "wind_degree": 220,
    "wind_dir": "SW",
    "pressure_mb": 1009,
    "pressure_in": 30.3,
    "precip_mm": 0.1,
    "precip_in": 0,
    "humidity": 82,
    "cloud": 75,
    "feelslike_c": 9.5,
    "feelslike_f": 49.2,
    "vis_km": 10,
    "vis_miles": 6,
    "uv": 1,
    "gust_mph": 10.5,
    "gust_kph": 16.9,
    "air_quality": {
      "co": 230.3,
      "no2": 13.5,
      "o3": 54.3,
      "so2": 7.9,
      "pm2_5": 8.6,
      "pm10": 11.3,
      "us-epa-index": 1,
      "gb-defra-index": 1
    }
  }
}

weather_data = WeatherModel(**data)

if __name__ == "__main__":
    print(weather_data)
