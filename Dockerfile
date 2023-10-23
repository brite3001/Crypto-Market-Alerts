FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./crypto_signal.py /code/crypto_signal.py
COPY ./binance_keys.yaml /code/binance_keys.yaml
COPY ./gotify_settings.yaml /code/gotify_settings.yaml
COPY ./top_50.yaml /code/top_50.yaml

ADD signal_generators /code/signal_generators/

CMD ["python3", "crypto_signal.py"]