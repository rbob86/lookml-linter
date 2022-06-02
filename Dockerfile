FROM python:3.8-slim-buster

COPY . .

#RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/./"

ENTRYPOINT python /linter/main.py
