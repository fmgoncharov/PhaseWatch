# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /PhaseWatch

COPY ../requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY docker .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]