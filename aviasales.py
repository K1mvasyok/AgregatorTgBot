import requests
import pprint
from datetime import datetime, timedelta

from config import api

async def tickets_for_day_with_neighbors(day, month, year, city_origin, city_destination):
    
    selected_tickets = []
    previous_tickets = []
    next_tickets = []
    
    for delta_day in [-1, 0, 1]: 
        query_date = datetime(year, month, day) + timedelta(days=delta_day)
        formatted_date = query_date.strftime("%Y-%m-%d")
        
        response = requests.get(f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?departure_at={formatted_date}&origin={city_origin}&destination={city_destination}&token={api}&calendar_type=departure_date&limit=100")
        response_json = response.json()
        
        if response_json['success'] == True:
            if delta_day == 0:
                selected_tickets.extend(response_json['data'])
            elif delta_day == -1:
                previous_tickets.extend(response_json['data'])
            elif delta_day == 1:
                next_tickets.extend(response_json['data'])
            
    selected_info, selected_links = format_ticket_info(selected_tickets)
    previous_info, previous_links = format_ticket_info(previous_tickets)
    next_info, next_links = format_ticket_info(next_tickets)
    
    return (selected_info, selected_links), (previous_info, previous_links), (next_info, next_links)

def format_flight_info(flight):
    duration_hours = flight['duration'] // 60
    duration_minutes = flight['duration'] % 60    
    
    departure_at = convert_from_rfc3339(flight['departure_at']).strftime("%d.%m.%Y %H:%M")  # Форматируем дату

    if flight['transfers'] == 0:
        transfers = "🛫 Прямой рейс\n"
    else:
        transfers = "🔄 С пересадкой\n"
    
    if duration_minutes == 0:
        duration_info = f"⏳ Длительность: {duration_hours} часов\n"
    else:
        duration_info = f"⏳ Длительность: {duration_hours} часов {duration_minutes} минут\n"
    
    return f"✈️ {flight['airline']} {flight['flight_number']}:\n" \
           f"🛫 {flight['origin']} ({flight['origin_airport']}) ➡️ {flight['destination']} ({flight['destination_airport']})\n" \
           f"🕒 Вылет: {departure_at}\n" \
           f"{transfers}" \
           f"{duration_info}" \
           f"💰 Цена: {flight['price']} ₽\n"


def format_ticket_info(ticket_data):
    flights_info = ''
    links = []
    for flight in ticket_data:
        flights_info += format_flight_info(flight)
        links.append(flight['link'])
    return flights_info, links
    
def convert_from_rfc3339(rfc3339_time):
    dt = datetime.fromisoformat(rfc3339_time.replace("Z", "+00:00"))
    return dt
