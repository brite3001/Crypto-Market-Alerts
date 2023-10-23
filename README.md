# Crypto Market Signals
Generates market signals based on the crypto market data. OHLCV data is grabbed from the python-binance API. Uses gotify to send signal notifications to my phone.


## Signals
At the moment I've got two signals implemented
- Signal 1: [The Altcoin Index](https://www.blockchaincenter.net/en/altcoin-season-index/)
- Signal 2: The average [Choppiness](https://www.tradingview.com/support/solutions/43000501980-choppiness-index-chop/) of the top 50 coins


## Crappy Getting Started
- Modify the binance_keys.yaml file with your [Binance API key](https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072) and secret. The only API restriction you need to tick is `Enable Reading`.
- Modify the gotify_settings.yaml with your base_url and app_token for your [gotify server](https://gotify.net/docs/install)

## Run the App
- `cd ~`
- `git clone https://github.com/brite3001/Crypto-Market-Alerts.git`
- `cd Crypto-Market-Alerts`
- `pip install poetry`
- `poetry install`
- `poetry shell`
- `python3 crypto_signals --signal alt_season --window 90 --candle 1d`

## Run the app with Docker
- `docker build -t crypto_signals .`
- `docker run -it crypto_signals --signal alt_season --window 90 --candle 1d`

## TODO
- ~~Dockerfile is broken, need to fix after the refactor~~
- App is probably really brittle, very little/no error checking
- ~~Add python args to select the signal you'd like to use~~
- ~~Add the args to Docker to select a signal~~
- Add some docs about using the container on docker and dockerswarm
- Investigate docker multistage builds with poetry

### Disclaimer
No signals generated by this app should be considered financial advice. I'm just doing this for fun. The signals could be completely wrong...