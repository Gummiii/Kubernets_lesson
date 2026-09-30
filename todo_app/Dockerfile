FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

ENV PORT=3000

CMD ["python", "app.py"]
