FROM python:3.12-slim

WORKDIR /app

COPY app/ ./app/
COPY requirements.txt .

RUN if [ -s requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["python", "app/main.py"]
