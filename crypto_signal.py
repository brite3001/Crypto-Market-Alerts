from gotify import Gotify
import schedule
import time
import yaml

from signal_generators import altcoin_index, choppy_index


def get_signal(
    gotify: Gotify, signal_type: str, sliding_window: int, candle_size: str
) -> None:
    advice = ""

    if signal_type == "alt_season":
        with open("top_50.yaml", "r") as f:
            data = yaml.safe_load(f)
        tickers = data["top_50"]
        advice = altcoin_index.generate_signal(tickers, sliding_window, candle_size)
    elif signal_type == "choppy_index":
        with open("top_50.yaml", "r") as f:
            data = yaml.safe_load(f)
        tickers = data["top_50"]
        advice = choppy_index.generate_signal(tickers, sliding_window, candle_size)

    gotify.create_message(
        message=advice,
        title=signal_type,
        priority=0,
    )

    print(f"Signal {signal_type} sent successfully")


def main():

    with open("gotify_settings.yaml", "r") as stream:
        data = yaml.safe_load(stream)

    gotify = Gotify(
        base_url=data["gotify_settings"]["base_url"],
        app_token=data["gotify_settings"]["app_token"],
    )

    signal_type = "choppy_index"
    sliding_window = 90
    candle_size = "1d"

    print("Started schedule")
    schedule.every(25).seconds.do(
        get_signal,
        gotify=gotify,
        signal_type=signal_type,
        sliding_window=sliding_window,
        candle_size=candle_size,
    )

    # schedule.schedule.every().day.at("10:00", "Australia/Victoria").do(
    #     get_signal, gotify=gotify, sliding_window=sliding_window
    # )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
