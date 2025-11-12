FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/backend

RUN pip install poetry==2.2.1
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

CMD ["tail", "-f", "/dev/null"]

# COPY . .

# CMD ["python", "main.py"]
# poetry run python  main.py
