import requests

# set up the API endpoint and headers
endpoint = "https://api.tdameritrade.com/v1/marketdata/{}/orderbook"
access_token = "Bearer y0fbcMLWPmZ/3JCQC6tLhiyvFqWusv5aMRnH6DsHLnGy0xTYx+djg2IxpmO8sJwF4soent/i1iVuIOVMsB5/dJGkKhacyGO1oGFMQ+lIKhRGB1M/6kqCFjc68hgiOLTS4/V2Gvq+Yr9z6Ze++5VymK8gzGzB7XuEbbJrh2AE6RxE8e1eO/BoY4lAIxVEAVQSpAQcx1HzC231OlwcTC7rxQI2cfiD1uPQWrPTIbfUP/b6d6TbBo0qk+7VrOj4CemZ87wLoLmszXIH/zFV0eYLR5MOlK43x22TQXkCjWWvUh/ON9o1IinO86yRDcaYryab6uyWFkSAKKekPstZDsT7Hw1TEUTBv55RDoE9YdfwFU2RBN7JNAQ4AMr54JPAyU0+ZHcJQ8h3caI4qhUk7mddyiOXpKzoL68axfCTx5mc2cvaz3QzhFrYWyo3sep872arL50rT9XcaTtnB/rZMx2TM52nEXc4XHoNJI6Df00rPcmHShul9HtsHAMj2zzef7jpKF4u11HGJEDUqjW8SO4KCxWw+zy3nGLURZFTy93bVXKkwHgaE100MQuG4LYrgoVi/JHHvl+pNCjt36YXoLK2sAS2xrp1LlwN4nGJ4PIe9Wb6B7Fvj4MNsFEQKIN3vNgMUHC9jMXmjJlye6H7zeYEG5liIYhPHxCnqVrqzTWlQzE96dNvR61fSrAjsQRKzaACuE/8ib6N1gKIR/37AkhSKghJzVpeLTZZKQ/Rhefjp7a6Ps17w7WCm8QDJlgtdwmAMasLM1n1mQVhb/k1V9jU2AjINMHktqUIPbq5QJlcwgwIhjbQIM+VMc8R87+4kuv/Zk4S/ZwOdVlLbgMUCsmXT6QNGx3Z1GsTG2jT0cqECziFQPnl0wuvQPoOkdLtxzjok+BRGoeLd4rGV6geuQ41LfPeS5XXQFLflM3szuppDMnzNR+1mF3jlQcx2Qwz5WvD7oXl533At/ZfR5OkodCXlaxZxb8zT0+3zpMLoKUC8mV5faHN4jRVyKNEJzNYRAyesIr2UzgQKnkwbIJ6OU7OvonlGEna4w1g+huwTw01+aYt5hUd/qCGWxmUTxRIP2sC9cZeIqNS+eq0Fenra6HhiuMt+v9e5vfucRQHu3AMZyF9eRUZCkbDdQ==212FD3x19z9sWBHDJACbC00B75E"

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

# specify the symbol of the asset you want to retrieve order book data for
symbol = "ORCL"

# make the GET request to the API endpoint
response = requests.get(endpoint.format(symbol), headers=headers)

# check the status code of the response
if response.status_code == 200:
    # parse the JSON response
    print(response)
    print(response.json())

else:
    print("Error:", response.status_code)

