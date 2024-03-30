import requests
import pprint

from datetime import datetime
from datetime import timedelta

from config import api

async def tickets_for_day(day, month, year, city_origin, city_destination):
    try:
        formatted_info_selected_day, links_selected_day = await get_tickets_for_specific_day(day, month, year, city_origin, city_destination)
        formatted_info_previous_day, links_previous_day = await get_tickets_for_day(day - 1, month, year, city_origin, city_destination)
        formatted_info_next_day, links_next_day = await get_tickets_for_day(day + 1, month, year, city_origin, city_destination)
    except Exception as e:
        return f"Произошла ошибка при получении билетов: {str(e)}", []

    formatted_info = ""
    all_links = []
    
    if formatted_info_selected_day:
        formatted_info += f"Билеты на выбранный день - {day}.{month}.{year}:\n{formatted_info_selected_day}\n\n"
        all_links.extend(links_selected_day)
    
    if formatted_info_previous_day:
        formatted_info += f"Билеты за день до - {day - 1}.{month}.{year}:\n{formatted_info_previous_day}\n\n"
        all_links.extend(links_previous_day)
    
    if formatted_info_next_day:
        formatted_info += f"Билеты за день после - {day + 1}.{month}.{year}:\n{formatted_info_next_day}\n\n"
        all_links.extend(links_next_day)
    
    if formatted_info:
        return formatted_info, all_links
    else:
        return f"Произошла ошибка при получении билетов: Нет доступных билетов на выбранный день и ближайшие дни", []

async def get_tickets_for_day(day, month, year, city_origin, city_destination):
    return await get_tickets_for_days(day, month, year, city_origin, city_destination, 0)

async def get_tickets_for_days(day, month, year, city_origin, city_destination, num_days):
    ticket_info_list = []
    target_day = datetime(year, month, day) + timedelta(days=num_days)
    try:
        formatted_info_day, links_day = await get_tickets_for_specific_day(target_day.day, target_day.month, target_day.year, city_origin, city_destination)
        if formatted_info_day:
            if num_days < 0:
                day_text = f"за {-num_days} {'день' if -num_days == 1 else 'дней'} {'до'}"
            else:
                day_text = f"{'на выбранный день' if num_days == 0 else f'за {num_days} день' if num_days == 1 else f'за {num_days} дней'} {'после' if num_days > 0 else 'до'}"
            ticket_info_list.append((day_text, formatted_info_day, links_day))
        else:
            ticket_info_list.append(("", []))
    except Exception as e:
        ticket_info_list.append(("", [])) 
    return ticket_info_list

async def get_tickets_for_specific_day(day, month, year, city_origin, city_destination):
    date_str = format_date(day, month, year)
    try:
        response_json = fetch_tickets(date_str, city_origin,city_destination)
        if response_json['success'] == True:
            formatted_info, links = format_ticket_info(response_json)
            return formatted_info, links
        else:
            return "", []
    except Exception as e:
        return "", []

def fetch_tickets(date_str, city_origin, city_destination):
    try:
        response = requests.get(f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?departure_at={date_str}&origin={city_origin}&destination={city_destination}&token={api}&calendar_type=departure_date&limit=100")
        return response.json()
    except Exception as e:
        return {"success": False}

def format_ticket_info(ticket_data):
    flights_info = ""
    links = []
    for flight in ticket_data['data']:
        flights_info += format_flight_info(flight)
        links.append(flight['link'])
    return flights_info, links

def format_flight_info(flight):
    duration_hours = flight['duration'] // 60
    duration_minutes = flight['duration'] % 60    
    departure_at = convert_from_rfc3339(flight['departure_at'])
    
    if flight['transfers'] == 0:
        transfers = "🛫 Прямой рейс\n"
    else:
        transfers = "🔄 С пересадкой\n"
    
    if duration_minutes == 0:
        duration_info = f"⏳ Длительность: {duration_hours} часов\n"
    else:
        duration_info = f"⏳ Длительность: {duration_hours} часов {duration_minutes} минут\n"
    
    return f"\n✈️ {flight['airline']} {flight['flight_number']}:\n" \
           f"🛫 {flight['origin']} ({flight['origin_airport']}) ➡️ {flight['destination']} ({flight['destination_airport']})\n" \
           f"🕒 Вылет: {departure_at}\n" \
           f"{transfers}" \
           f"{duration_info}" \
           f"💰 Цена: {flight['price']} ₽\n" 

def format_date(day, month, year):
    day_str = f"0{day}" if day < 10 else f"{day}"
    month_str = f"0{month}" if month < 10 else f"{month}"
    return f"{year}-{month_str}-{day_str}"

def convert_from_rfc3339(rfc3339_time):
    dt = datetime.fromisoformat(rfc3339_time.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%d %H:%M:%S")

