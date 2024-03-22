
import hashlib
import hmac
import time

import requests

#API Key: AJ14jFXUZwB9gLvv
#API Secret: viwih1ugG3gclxhma6XM55RY2KfqCk25

secretKey = 'viwih1ugG3gclxhma6XM55RY2KfqCk25'
access_key = 'AJ14jFXUZwB9gLvv'

timestamp = str(int(time.time()))
message = timestamp + 'GET' + '/api/v3/brokerage/products/ETH-USD'
signature = hmac.new(secretKey.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
print(signature.hex())


url = "https://api.coinbase.com/api/v3/brokerage/products/ETH-USD"

headers = {
    "accept": "application/json",
    "CB-ACCESS-KEY": access_key,
    "CB-ACCESS-SIGN": str(signature.hex()),
    "CB-ACCESS-TIMESTAMP": timestamp
}

response = requests.get(url, headers=headers)

print(response.text)

