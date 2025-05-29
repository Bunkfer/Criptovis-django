FROM bunkfer/django:3.13.3-slim

WORKDIR /app

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
