from collections import Counter
import json
import os
import requests

from pendulum import today
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.getenv('SLACK_TOKEN'))

def get_ticket_sales(url):
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
    

response = get_ticket_sales('https://api.tito.io/v3/datatuneconf/nashville-2024/tickets?page[size]=1000')
registration_counts = Counter(i['release_title'] for i in response['tickets']).most_common()
message = '\n'.join([':white_circle: ' + i[0] + ': ' + str(i[1]) for i in registration_counts])

channel_id = "C05L51TPK7T"

try:
    result = client.chat_postMessage(
        channel=channel_id,
        text=f':admission_tickets: Ticket sales breakdown as of {today().format("MMMM DD, YYYY")} :admission_tickets:\n\n{message}'
    )

except SlackApiError as e:
    print(f"Error: {e}")
