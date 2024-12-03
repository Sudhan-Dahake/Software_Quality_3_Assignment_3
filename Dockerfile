FROM python:3.11.4-slim

WORKDIR /app

COPY . .

RUN rm rf __pycache__ .github .idea

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0"]