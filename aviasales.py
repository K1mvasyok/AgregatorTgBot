import requests

from config import api, marker

response = requests.get(f'https://{api}.travelpayouts.com/aviasales/v3/prices_for_dates')