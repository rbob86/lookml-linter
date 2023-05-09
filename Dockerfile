FROM python:3.10-slim-buster
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/./"
ENTRYPOINT python /linter/main.py
