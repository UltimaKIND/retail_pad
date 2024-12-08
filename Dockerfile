FROM python:3.12.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY ./pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main --no-root
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
COPY . .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]