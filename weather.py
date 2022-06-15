import requests
from secret import OWM_TOKEN
url = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    response = requests.get(
        url,
        params={
            'q': city,
            'appid': OWM_TOKEN,
            'units': 'metric',
        }
    )
    d = response.json()
    return f'Air temperature in {city} is {round(d["main"]["temp"], 1)}°C, {d["weather"][0]["description"]}'


if __name__ == '__main__':
    import sys
    city = ' '.join(sys.argv[1:])
    if not city:
        city = 'Helsinki'
