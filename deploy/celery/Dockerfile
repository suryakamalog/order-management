FROM python:3.12.1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Install and configure the message broker (e.g., Redis)
# ... (specific steps depending on the chosen message broker)

CMD ["celery", "-A", "app.app:celery_app", "worker", "-l", "info"]
