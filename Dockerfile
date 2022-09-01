FROM python:3.10.5-bullseye

COPY . .


RUN pip install -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/./"

ENTRYPOINT python /linter/main.py
