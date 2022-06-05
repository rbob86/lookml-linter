FROM python:3.8-slim-buster
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/./"
ENTRYPOINT python /linter/main.py