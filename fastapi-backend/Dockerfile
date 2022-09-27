FROM python:3.10

WORKDIR /code/app

RUN pip install uvicorn fastapi alembic tenacity sqlalchemy psycopg2

COPY ./ /code/app

EXPOSE 80
CMD ["bash", "start.sh"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--reload"]