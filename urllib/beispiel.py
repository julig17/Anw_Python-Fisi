import json
import urllib.request

url = "https://api.open-meteo.com/v1/forecast?latitude=50.1109&longitude=8.6821&current_weather=true"

try:
    with urllib.request.urlopen(url) as webURL:
        data = webURL.read() 
        json_data = json.loads(data.decode('utf-8'))
        print(json_data["current_weather"]["temperature"])
except urllib.error.URLError as e:
    print(f"Fehler beim Zugriff auf die URL: {e.reason}")