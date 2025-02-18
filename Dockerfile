FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY sales_agent.py .
COPY sales_tools.py .
COPY product_catalog.json .
COPY templates/ ./templates/

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV STRIPE_API_KEY=${STRIPE_API_KEY}

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]