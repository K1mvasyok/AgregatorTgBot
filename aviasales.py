import requests

from config import api, marker

response = requests.get('https://api.travelpayouts.com/aviasales/v3/prices_for_dates')