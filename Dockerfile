FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app/mysite/
COPY requirements.txt .
RUN pip install -r requirements.txt
