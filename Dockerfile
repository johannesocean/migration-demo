FROM python:3.9

WORKDIR /api

COPY app app
COPY ./requirements.txt requirements.txt
COPY ./alembic.ini alembic.ini

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 2512
CMD uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 2512
