from web3 import Web3

def connect():
    return Web3(Web3.HTTPProvider(RPC_URL))
