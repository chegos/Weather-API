from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_weather(city):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={API_KEY}"
    
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()

@app.route("/weather")
def get_weather():
    city = request.args.get("city")

    data = fetch_weather(city)

    if not data:
        return jsonify({"error": "Cidade não encontrada"}), 404

    current = data.get("currentConditions", {})

    return jsonify({
        "city": city,
        "temperature": current.get("temp"),
        "condition": current.get("conditions"),
        "humidity": current.get("humidity"),
        "wind_speed": current.get("windspeed")
    })

if __name__ == "__main__":
    app.run(debug=True)
