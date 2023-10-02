from binance.client import Client
import yaml

with open("binance_keys.yaml", "r") as stream:
        data = yaml.safe_load(stream)

client = Client(
    data["binance_keys"]["api_key"],
    data["binance_keys"]["api_secret"],
)

def get_candle_data(ticker: str, candle_size: str, num_candles: int) -> list:
    """
    API call returns data formatted like this:
    list of OHLCV values
    (Open time, Open, High, Low, Close, Volume, Close time, Quote asset volume,
    Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)
    """
    formatted_response = []
    api_reponse_format = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
        "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume",
        "ignore",
    ]

    unformatted_response = client.get_historical_klines(
        symbol=ticker, limit=num_candles, interval=candle_size
    )

    for candle in unformatted_response:
        candle_with_labels = {}
        for value, description in zip(candle, api_reponse_format):
            candle_with_labels[description] = value

        formatted_response.append(candle_with_labels)

    return formatted_response


def get_ohlcv_from_candles(candles: list) -> dict:
    ohlcv = {
        "open": [],
        "high": [],
        "low": [],
        "close": [],
        "volume": [],
    }

    for candle in candles:
        ohlcv["open"].append(candle["open"])
        ohlcv["high"].append(candle["high"])
        ohlcv["low"].append(candle["low"])
        ohlcv["close"].append(candle["close"])
        ohlcv["volume"].append(candle["volume"])

    return ohlcv