from flask import Flask, jsonify
import requests

app = Flask(__name__)

WEATHER_API_KEY = '4adca2fd361e4686abf141627243004'
WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'


@app.route('/toolshedWeatherApi/<city>')
def get_weather(city):
    try:

        response = requests.get(WEATHER_API_URL, params={'key': WEATHER_API_KEY, 'q': city})
        response.raise_for_status()
        data = response.json()

        weather_data = [{
            'location': data['location']['name'],
            'region': data['location']['region'],
            'country': data['location']['country'],
            'lat': data['location']['lat'],
            'lon': data['location']['lon'],
            'temp_c': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'wind_kph': data['current']['wind_kph'],
            'humidity': data['current']['humidity'],
            'cloud': data['current']['cloud'],
            'feelslike_c': data['current']['feelslike_c']
        }]

        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
