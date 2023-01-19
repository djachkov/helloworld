# The foundation https://github.com/wemake-services/wemake-django-template
FROM python:3.11.1-slim-buster as builder
ENV POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local' \
    PIP_NO_CACHE_DIR=on
RUN apt-get update && apt-get upgrade -y \
    curl \
    && apt-get install --no-install-recommends -y \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*
WORKDIR /src

COPY ./poetry.lock ./pyproject.toml /src/
RUN poetry version \
    && poetry install

FROM python:3.11.1-slim-buster
# USER backend
WORKDIR /src
# COPY --from=builder /var/cache/pypoetry /var/cache/pypoetry
COPY --from=builder /usr/local /usr/local
COPY ./main.py /src/

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]