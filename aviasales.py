import requests
import pprint
from datetime import datetime

from config import api

async def tickets_for_day(day, month, year, city_origin, city_destination):
    
    if month < 10:
        month = f"0{month}"
    else:
        month = f"{month}"
    if day < 10:
        day = f"0{day}"
    else:
        day = f"{day}"
        
    response = requests.get(f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?departure_at={year}-{month}-{day}&origin={city_origin}&destination={city_destination}&token={api}&calendar_type=departure_date&limit=30")
    response_json = response.json()
    if response_json['success'] == True:
        formatted_info, links = format_ticket_info(response_json)
        pprint.pprint(response_json)
        return formatted_info, links
    else:
        return "ℹ️ Информация о билете: Нет доступных билетов", []
            
def format_flight_info(flight):
    
    duration_hours = flight['duration'] // 60
    duration_minutes = flight['duration'] % 60    
    
    departure_at = convert_from_rfc3339(flight['departure_at'])
    
    return f"\n✈️ {flight['airline']} {flight['flight_number']}:\n" \
           f"🛫 {flight['origin']} ({flight['origin_airport']}) ➡️ {flight['destination']} ({flight['destination_airport']})\n" \
           f"🕒 Вылет: {departure_at}\n" \
           f"⏳ Длительность: {duration_hours} часов {duration_minutes} минут\n" \
           f"💰 Цена: {flight['price']} ₽\n" 

def format_ticket_info(ticket_data):
    if ticket_data['data']:
        flights_info = '\n'.join([format_flight_info(flight) for flight in ticket_data['data']])
        links = [flight['link'] for flight in ticket_data['data']]
        return f"ℹ️ Информация о билете:\n{flights_info}", links
    else:
        return "ℹ️ Информация о билете: Нет доступных билетов", []
    
def convert_from_rfc3339(rfc3339_time):
    dt = datetime.fromisoformat(rfc3339_time.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%d %H:%M:%S")