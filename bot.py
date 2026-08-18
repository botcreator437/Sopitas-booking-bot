import requests
import json

URL = "https://gestionreservas.victoriarestauracion.es/reservas/admin/ApiVisitasV2/disponibilidad_bodega"

payload = {
    "bodega": "46",
    "adultos": 2,
    "lista": {"1": 2},
    "fecha": "23/08/2026",
    "servicio": "31",
    "idioma": "1"
}

response = requests.post(
    URL,
    json=payload,
    headers={"Content-Type": "application/json"},
    timeout=30
)

print("Status:", response.status_code)
print("Response:")
print(response.text)
