FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app
COPY  . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]