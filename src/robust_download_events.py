import requests
import pandas as pd
import os
import time
import json

BASE = "https://premier.72-60-245-2.sslip.io"
DATA_FILE = "data/events.csv"
CHUNK_SIZE = 25000
TOTAL_EVENTS = 444252

def download_paginated():
    os.makedirs("data", exist_ok=True)
    
    # Check if file exists and how many rows it has (excluding header)
    if os.path.exists(DATA_FILE):
        try:
            # We count lines because we want to resume
            with open(DATA_FILE, 'r') as f:
                row_count = sum(1 for line in f) - 1
            if row_count < 0: row_count = 0
            start_offset = row_count
            print(f"Resuming from offset {start_offset}...")
        except Exception:
            start_offset = 0
    else:
        start_offset = 0

    mode = 'a' if start_offset > 0 else 'w'
    header = True if start_offset == 0 else False

    for offset in range(start_offset, TOTAL_EVENTS, CHUNK_SIZE):
        limit = min(CHUNK_SIZE, TOTAL_EVENTS - offset)
        url = f"{BASE}/events?limit={limit}&offset={offset}"
        
        retries = 5
        success = False
        while retries > 0 and not success:
            try:
                print(f"Fetching {limit} events at offset {offset}...")
                response = requests.get(url, timeout=60)
                response.raise_for_status()
                data = response.json()
                events = data.get('events', [])
                
                if events:
                    df = pd.DataFrame(events)
                    # Qualifiers need to be stringified for CSV compatibility like the official export
                    if 'qualifiers' in df.columns:
                        df['qualifiers'] = df['qualifiers'].apply(json.dumps)
                    
                    df.to_csv(DATA_FILE, index=False, header=header, mode=mode)
                    header = False
                    mode = 'a'
                    success = True
                    print(f"Saved chunk to {DATA_FILE}. Total rows ≈ {offset + len(events)}")
                else:
                    success = True # No more events?
            except Exception as e:
                print(f"Error at offset {offset}: {e}. Retrying in 5s... ({retries} left)")
                time.sleep(5)
                retries -= 1
        
        if not success:
            print("Failed to download chunk after multiple retries. Stop.")
            break

if __name__ == "__main__":
    download_paginated()
