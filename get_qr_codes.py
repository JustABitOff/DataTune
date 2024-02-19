from pathlib import Path
import requests

from PIL import Image

from tito import Tito


def _convert_slug_to_qr_code_url(slug: str) -> str:
    return f'https://qr.tito.io/tickets/{slug}/vcard'

def _make_vcards_directory():
    Path('vcards').mkdir(parents=True, exist_ok=True)

def main():
    tito_instance = Tito()
    tickets = tito_instance.tickets()

    _make_vcards_directory()

    for i in range(len(tickets)):
        slug = tickets[i]['slug']
        Image.open(
            requests.get(
                _convert_slug_to_qr_code_url(slug),
                stream=True
            ).raw
        ).save(f'vcards/{slug}.png')
        
        print(f'>>> Progress: Stored {slug}....{i+1} of {len(tickets)}')

if __name__ == '__main__':
    main()
