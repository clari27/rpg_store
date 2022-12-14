FROM python:3.8-slim-buster

WORKDIR /app

COPY  . .

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]