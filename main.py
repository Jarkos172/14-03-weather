from services.excel_files import save_to_excel
from services.openweather_api import get_weather
from services.dashboard import render_dashboard
import time



while True:
      weather = get_weather("glasgow")
      save_to_excel([weather])
      print("pobieram i zapisuje dane")

      render_dashboard('lisbon1.xlsx')
      time.sleep(10)


