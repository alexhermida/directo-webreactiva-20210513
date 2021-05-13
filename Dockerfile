FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt