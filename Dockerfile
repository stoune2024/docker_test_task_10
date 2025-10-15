FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN apt-get update -y && apt-get install -y gcc libpq-dev iputils-ping && pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

CMD ["python", "/app/app/main.py"]
