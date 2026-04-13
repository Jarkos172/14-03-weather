import requests
from datetime import datetime
#from common.tools import kelvin_na_celsjusze
#from common.tools import ms_na_kmh

def get_weather(city):

    API_KEY =  "fe050a1d49ebee3f3b240c565ce08b27"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        record = {
            "city": data.get("name"),
            "temp":  data.get("main").get("temp"),
            "feels_like": data.get("main").get("feels_like"),
            "wind": data.get("wind").get("speed"),
            "timestamp": datetime.now().strftime("%Y-%m-%du %H:%M:%S"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "description": data.get("weather")[0].get("description")
        }

        return record


    except Exception as e:
        print(e)



