# Crypto signal Generator
Generates market signals based on the crypto market. Uses gotify to send signal notifications.
My main usecase for this app is to get a broad view of the state of the crypto market. I want a good idea about what's happening when I wake up in the morning.
I'm thinking of deploying multiple instances of this container, with a simple switch to change the signal being generated.


## Signals
At the moment I've got two signals implemented
- Signal 1: [The Altcoin Index](https://www.blockchaincenter.net/en/altcoin-season-index/)
- Signal 2: The [Choppiness](https://www.tradingview.com/support/solutions/43000501980-choppiness-index-chop/) of the top 50 coins


## Crappy Getting Started
- Modify the binance_keys.yaml file with your Binance API key and secret
- Modify the gotify_settings.yaml with your base_url and app_token for your gotify server

## Run the App
- `cd ~`
- `git clone https://github.com/brite3001/Crypto-Market-Alerts.git`
- `cd Crypto-Market-Alerts`
- `python3 -m venv env`
- `source env/bin/activate`
- `python3 crypto_signal.py`

## TODO
- Dockerfile is broken, need to fix after the refactor
- Add is probably really brittle, very little/no error checking
- Add python args to select the signal you'd like to use
- Add the args to Docker to select a signal
- Add some docs about using the container on docker and dockerswarm