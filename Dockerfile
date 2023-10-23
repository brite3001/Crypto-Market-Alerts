FROM python:3.10

RUN pip install poetry==1.3.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY ./crypto_signal.py /code/crypto_signal.py
COPY ./binance_keys.yaml /code/binance_keys.yaml
COPY ./gotify_settings.yaml /code/gotify_settings.yaml
COPY ./top_50.yaml /code/top_50.yaml
ADD signal_generators /code/signal_generators/

RUN poetry install --without dev

ENTRYPOINT ["poetry", "run", "python3", "crypto_signal.py"]