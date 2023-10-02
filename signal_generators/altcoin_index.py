from . import binance_helpers
import yaml



def calculate_performance(ohlcv: dict) -> float:
    start_price = float(ohlcv["close"][0])
    end_price = float(ohlcv["close"][-1])
    return ((end_price - start_price) / start_price) * 100


def generate_signal(tickers: list, sliding_window: int, candle_size: str) -> str:
    performed_better_than_btc = 0
    btc_performance = 0
    advice = ''

    btc_candles = binance_helpers.get_candle_data(
        ticker="BTCUSDT", num_candles=sliding_window, candle_size=candle_size
    )
    btc_ohlcv = binance_helpers.get_ohlcv_from_candles(btc_candles)
    btc_performance = calculate_performance(btc_ohlcv)

    # print(f"Btc Price movement past {sliding_window} days {btc_performance}")

    for alt_coin in tickers:
        alt_candles = binance_helpers.get_candle_data(
            ticker=alt_coin, num_candles=sliding_window, candle_size="1d"
        )

        alt_ohlcv = binance_helpers.get_ohlcv_from_candles(alt_candles)
        alt_performance = calculate_performance(alt_ohlcv)

        if alt_performance > btc_performance:
            performed_better_than_btc += 1
            # print(f"Alt coin {alt_coin} performed better than BTC! {alt_performance}")

    alt_coin_index = int((performed_better_than_btc / len(tickers)) * 100)

    if alt_coin_index >= 75:
        advice = f"Altcoin Index = {alt_coin_index}, ALT BULL MARKET IS HERE!"
    else:
        advice = f"Altcoin Index = {alt_coin_index}, not alt bull market"

    return advice



