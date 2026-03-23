import requests
import os
import time

BASE = "https://premier.72-60-245-2.sslip.io"
endpoints = [
    ("/export/players", "data/players.csv"),
    ("/export/matches", "data/matches.csv"),
    ("/export/events", "data/events.csv"),
    ("/export/player_history", "data/player_history.csv")
]

os.makedirs("data", exist_ok=True)

for endpoint, filename in endpoints:
    url = f"{BASE}{endpoint}"
    print(f"Downloading {url} to {filename}...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
