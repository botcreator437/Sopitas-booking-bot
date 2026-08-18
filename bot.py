import os
import requests

API_URL = "https://gestionreservas.victoriarestauracion.es/reservas/admin/ApiVisitasV2/disponibilidad_bodega"

payload = {
    "bodega": "46",
    "adultos": 2,
    "lista": {"1": 2},
    "fecha": "23/08/2026",
    "servicio": "31",
    "idioma": "1"
}

response = requests.post(
    API_URL,
    json=payload,
    headers={"Content-Type": "application/json"},
    timeout=30
)

data = response.json()

print("Status:", response.status_code)
print("Response:", response.text)

times = data.get("horariostexto", [])

available_times = []

for time in times:
    hour, minute = map(int, time.split(":"))
    total_minutes = hour * 60 + minute

    if total_minutes > 13 * 60 + 15:
        available_times.append(time)

if not available_times:
    print("No availability after 13:15.")
    exit()

print("Available times after 13:15:", available_times)

token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

message = (
    "🍽️ Sopitas — AVAILABILITY!\n\n"
    "Date: 23 August 2026\n"
    "Guests: 2\n"
    f"Available times after 13:15: {', '.join(available_times)}"
)

telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"

telegram_response = requests.post(
    telegram_url,
    data={
        "chat_id": chat_id,
        "text": message
    },
    timeout=30
)

print("Telegram status:", telegram_response.status_code)
print("Telegram response:", telegram_response.text)
print("Telegram notification sent.")
