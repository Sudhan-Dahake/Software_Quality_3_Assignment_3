FROM python:3.11.4-slim

WORKDIR /app

COPY . .

RUN rm -rf __pycache__ .github .idea

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/keep_alive.sh

RUN apt-get update && apt-get install -y curl supervisor && apt-get clean

# Exposing a PORT
EXPOSE 8000

CMD ["supervisord", "-c", "/app/supervisord.conf"]