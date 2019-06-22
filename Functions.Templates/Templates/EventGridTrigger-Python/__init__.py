import logging
from datetime import datetime

import azure.functions as func


def main(event: func.EventGridEvent):

    event_id: str = event.id
    event_data: dict = event.get_json()
    event_topic: str = event.topic
    event_subject: str = event.subject
    event_type: str = event.event_type
    event_time: datetime = event.event_time
    event_data_version: str = event.event_data_version

