from collections import Counter
import json
import os
import requests

from pendulum import today
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from api.tito import Tito

client = WebClient(token=os.getenv('SLACK_TOKEN'))

tito_instance = Tito()
tickets = tito_instance.tickets()
registration_counts = Counter(i['release_title'] for i in tickets).most_common()
message = '\n'.join([':white_circle: ' + i[0] + ': ' + str(i[1]) for i in registration_counts])

channel_id = "C05L51TPK7T"

try:
    result = client.chat_postMessage(
        channel=channel_id,
        text=f':admission_tickets: Ticket sales breakdown as of {today().format("MMMM DD, YYYY")} :admission_tickets:\n\n{message}'
    )

except SlackApiError as e:
    print(f"Error: {e}")
