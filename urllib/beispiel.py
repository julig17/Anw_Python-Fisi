import json
import urllib.request, urllib.error

url = "https://api.open-meteo.com/v1/forecast?latitude=50.1109&longitude=8.6821&current_weather=true"

try:
    with urllib.request.urlopen(url) as webURL:
        data = webURL.read()
        print(data)
        json_data = json.loads(data)
        print(json_data["current_weather"]["temperature"])
except urllib.error.URLError as e:
    print(f"Schiefgegangen bei Abfragen Netzwerkresource {e}")