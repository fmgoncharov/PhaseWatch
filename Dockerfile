# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /PhaseWatch

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY Dockerfile .
COPY echo_bot.py echo_bot.py
COPY echo_bot.py .
COPY echo_bot.py echo_bot

CMD [ "python3", "echo_bot.py"]
