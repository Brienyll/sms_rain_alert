import requests
from twilio.rest import Client


OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
API_key = "52e8bcf0cf64b215fd6d939a6f76ed98"
account_sid = 'ACbe4a1e679e4eeaf6e7ff595332cc274f'
auth_token = '699fd8b09d6ff02181c6e7e50c646495'

weather_params = {
    "lat": -21.354,
    "lon": -51.8562,
    "appid": API_key
}

response = requests.get(OWM_endpoint, params=weather_params)
data = response.json()
weather_id = data["weather"][0]["id"]
if weather_id < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an Umbrella! ☔",
        from_='+15087948043',
        to='+18059917066'
    )

    print(message.sid)
    print("Bring an Umbrella!")
print(data["weather"][0]["id"])
