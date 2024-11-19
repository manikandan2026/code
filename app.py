from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY ="7040ea904442a45d6950ba584410ce59"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            city = city.strip().title()  # Clean and format the input
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)

            if response.status_code == 200:
                weather_data = response.json()
            elif response.status_code == 404:
                weather_data = {"error": "City not found! Please check the name."}
            else:
                weather_data: dict[str, str] = {"error": f"API error: {response.status_code}"}

    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
