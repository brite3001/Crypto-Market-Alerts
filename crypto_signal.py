from gotify import Gotify
import schedule
import time
import yaml
import argparse

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
    else:
        print('Didnt recognise the signal type!')

    if len(advice) != 0:
        gotify.create_message(
            message=advice,
            title=signal_type,
            priority=0,
        )

        print(f"Signal {signal_type} sent successfully")
    else:
        print('No advice to send!')


def main():

    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--signal', required=True,
                    type=str, metavar='SIGNAL_TYPE',
                    choices=['alt_season', 'choppy_index'],
                    help="What signal do you want to calculate?")

    p.add_argument('--window', required=True,
                    type=int, metavar='WINDOW_SIZE',
                    choices=range(14, 365),
                    help="What should the window size be for the signal calculation?")
    
    p.add_argument('--candle', required=True,
                    type=str, metavar='CANDLE_SIZE',
                    choices=['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1m'],
                    help="What candle size would you like the ohlcv data for?")


    args = p.parse_args()

    with open("gotify_settings.yaml", "r") as stream:
        data = yaml.safe_load(stream)

    gotify = Gotify(
        base_url=data["gotify_settings"]["base_url"],
        app_token=data["gotify_settings"]["app_token"],
    )

    signal_type = args.signal
    sliding_window = args.window
    candle_size = args.candle

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
