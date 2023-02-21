from flask import Flask, request
import json
from binance.um_futures import UMFutures as Client


app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']

        params = {
            "symbol": ticker,
            "side": side,
            "positionSide": "SHORT",
            "type": "MARKET",
            "quantity": quantity,
        }

        params2 = {
            "symbol": ticker,
            "side": side,
            "positionSide": "LONG",
            "type": "MARKET",
            "quantity": quantity,
        }

        if side == "BUY":
            Client(binanceApiKey, binanceSecretKey).new_order(**params2)
        if side == "SELL":
            Client(binanceApiKey, binanceSecretKey).new_order(**params)



    except:
        pass
    return {
        "code": "success",
    }










