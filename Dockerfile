FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/mysite/
WORKDIR /app/mysite/
RUN pip install -r requirements.txt
