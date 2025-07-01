import requests
from config import READSB_URL

def fetch_aircraft_data():
    resp = requests.get(READSB_URL, timeout=2)
    resp.raise_for_status()
    return resp.json()
