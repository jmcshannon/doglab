FROM python:3.13.3-slim

COPY requirements.txt .

RUN pip install -r requirements.txt