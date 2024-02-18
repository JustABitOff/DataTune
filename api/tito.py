import json
import os
import requests


class Tito:

    def __init__(self) -> None:
        self.url = 'https://api.tito.io'
        self.api_version = 'v3'
        self.tito_account = 'datatuneconf'
        self.tito_event = 'nashville-2024'
        self.base_url = self._get_call_base_url()
        self.__api_token = os.getenv('TITO_TOKEN')

    def _get_call_base_url(self) -> str:
        return f'{self.url}/{self.api_version}/{self.tito_account}/{self.tito_event}'

    def tickets(self) -> str:
        try:
            response = requests.get(
                f'{self.base_url}/tickets?page[size]=1000',
                headers={
                    'Accept': 'application/json',
                    'Authorization': f'Token token={self.__api_token}'
                }
            )

            if response.status_code == 200:
                data_dict = json.loads(response.text)
                return data_dict['tickets']
            else:
                response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
