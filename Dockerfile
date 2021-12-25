# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /PhaseWatch

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY Dockerfile .
COPY phase_watch_bot.py phase_watch_bot.py

CMD [ "python3", "phase_watch_bot.py"]
