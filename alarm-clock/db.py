from sqlmodel import create_engine, Session, SQLModel, select
from model import Alarm

engine = create_engine("sqlite:///database.db", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_alarm(hour: int, minute: int) -> Alarm:
    if not (0 <= hour < 24) or not (0 <= minute < 60):
        raise ValueError("Hour must be in range [0, 24). Minute must be in range [0, 60)")

    with Session(engine) as session:
        alarm = session.exec(
            select(Alarm).where(Alarm.hour == hour, Alarm.minute == minute)
        ).first()

        if alarm:
            alarm.active = True
        else:
            alarm = Alarm(hour=hour, minute=minute)

        session.add(alarm)
        session.commit()
        session.refresh(alarm)

    return alarm
