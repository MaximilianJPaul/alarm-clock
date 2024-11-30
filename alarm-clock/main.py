import argparse
import sys

from utils import alarm_to_datetime, play_alarm
from datetime import datetime
from db import engine, create_db_and_tables, create_alarm
from sqlmodel import Session, select
from model import Alarm


def main():
    with Session(engine) as session:
        alarms = session.exec(select(Alarm)).all()

    while True:
        current_time = datetime.now()
        for alarm in alarms:
            date = alarm_to_datetime(alarm)
            if date.hour == current_time.hour and date.second == current_time.second:
                play_alarm()


if __name__ == "__main__":
    create_db_and_tables()

    parser = argparse.ArgumentParser(description="Alarm Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="subcommands")

    set_alarm_parser = subparsers.add_parser("set-alarm", help="Set an alarm")
    set_alarm_parser.add_argument("hour", type=int, help="Hour for the alarm (0-23)")
    set_alarm_parser.add_argument("minute", type=int, help="Minute for the alarm (0-59)")

    args = parser.parse_args()

    if args.command == "set-alarm":
        alarm = create_alarm(args.hour, args.minute)
        sys.exit(0)

    main()