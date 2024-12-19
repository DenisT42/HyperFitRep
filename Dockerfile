FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential

RUN pip install -U pip
RUN pip install uvicorn fastapi jinja2 sqlalchemy pydantic asyncmy

WORKDIR /app

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
