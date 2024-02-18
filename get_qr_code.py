from PIL import Image

import json
import os
from pathlib import Path
import requests


def _convert_slug_to_qr_code_url(slug: str) -> str:
    return f'https://qr.tito.io/tickets/{slug}/vcard'

def _get_all_tito_tickets(url: str) -> list:
    try:
        response = requests.get(
            url,
            headers={
                'Accept': 'application/json',
                'Authorization': f'Token token={os.getenv("TITO_TOKEN")}'
            }
        )

        if response.status_code == 200:
            data_dict = json.loads(response.text)
            return data_dict
        else:
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


tickets = _get_all_tito_tickets(
    url = 'https://api.tito.io/v3/datatuneconf/nashville-2024/tickets?page[size]=1000'
)
Path('vcards').mkdir(parents=True, exist_ok=True)
for ticket in tickets['tickets']:
    slug = ticket['slug']
    img = Image.open(
        requests.get(
            _convert_slug_to_qr_code_url(slug),
            stream=True
        ).raw
    ).save(f'vcards/{slug}.png')