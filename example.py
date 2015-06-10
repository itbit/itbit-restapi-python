from itbit_api import itBitApiConnection
import json

client_key = '< client key >'
secret_key = '< secret key >'
userId = '< userId >'

#create the api connection
itbit_api_conn = itBitApiConnection(clientKey=client_key, secret=secret_key, userId=userId)

#get all the wallets for the user
wallets = itbit_api_conn.get_all_wallets().json()

#get the id of the wallet named Wallet
walletId = next(wallet for wallet in wallets if wallet['name'] == 'Wallet')['id']

#print the trades for the selected wallet
print(json.dumps(itbit_api_conn.get_wallet_trades(walletId).json(), indent=2))

