import json
import os
import requests

from pendulum import today
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.getenv('SLACK_TOKEN'))

def get_sessionize_sessions(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data_dict = json.loads(response.text)
            return data_dict
        else:
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    

response = get_sessionize_sessions('https://sessionize.com/api/v2/q4frvnyx/view/Sessions')
number_of_sessions = len(response[0].get('sessions'))

channel_id = "C05L51TPK7T"

try:
    result = client.chat_postMessage(
        channel=channel_id,
        text=f'{number_of_sessions} sessions have been submitted as of {today().format("MMMM DD, YYYY")} :partying_face:'
    )

except SlackApiError as e:
    print(f"Error: {e}")
