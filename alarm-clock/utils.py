import time

from datetime import datetime, timedelta
from model import Alarm


def play_alarm(interval: float = 1):
    for i in range(10):
        print('\a', end='', flush=True)
        time.sleep(interval)


def alarm_to_datetime(alarm: Alarm) -> datetime:
    current_time = datetime.now()

    if alarm.hour > current_time.hour or (alarm.hour == current_time.hour and alarm.minute > current_time.minute):
        target_date = current_time
    else:
        target_date = current_time + timedelta(days=1)

    date = datetime(
        year=target_date.year,
        month=target_date.month,
        day=target_date.day,
        hour=alarm.hour,
        minute=alarm.minute,
        second=0,
        microsecond=0,
    )

    return date
