from . import binance_helpers

from talipp.indicators import CHOP
from talipp.ohlcv import OHLCVFactory


def calculate_chop(ohlcv: dict) -> int:
    # CHOPINESS CALCULATION
    ohlcv["high"] = [float(x) for x in ohlcv["high"]]
    ohlcv["low"] = [float(x) for x in ohlcv["low"]]
    ohlcv["close"] = [float(x) for x in ohlcv["close"]]

    ohlcv_factory = OHLCVFactory.from_dict(
        {
            "high": ohlcv["high"][-14:],
            "low": ohlcv["low"][-14:],
            "close": ohlcv["close"][-14:],
        }
    )

    chop = CHOP(14, ohlcv_factory)
    return chop[0]


def generate_signal(tickers: list, sliding_window: int, candle_size: str) -> str:
    advice = ""
    chops = []

    for alt_coin in tickers:
        alt_candles = binance_helpers.get_candle_data(
            ticker=alt_coin, num_candles=sliding_window, candle_size="1d"
        )

        alt_ohlcv = binance_helpers.get_ohlcv_from_candles(alt_candles)
        chops.append(calculate_chop(alt_ohlcv))

    avg_chop = round(sum(chops) / len(chops), 1)

    if avg_chop >= 61.8:
        advice = f"Choppiness Index = {avg_chop}, market is CHOPPY!!"
    elif avg_chop <= 38.2:
        advice = f"Choppiness Index = {avg_chop}, market is TRENDING!!"
    else:
        advice = f"Choppiness Index = {avg_chop}, market is undecided"

    return advice
