
# POST to lh_ms_activity_price
import requests
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("XANO_BASE_URL", "https://xano.io/api/v1")
api_key = os.getenv("XANO_API_KEY", "")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Build payload based on table schema
payload = {
    # "id": integer (auto-generated, omit on POST)
    # "created_at": timestamp (auto-generated, omit on POST)
    "currency": "example_value",  # integer
    "total": "example_value",  # integer
}

url = f"{base_url}/tables/lh_ms_activity_price"

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"Success: {response.status_code}")
    print(response.json())
except requests.RequestException as e:
    print(f"Error: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Response: {e.response.text}")
