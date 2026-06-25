from web3 import Web3

RPC_URL = "https://mainnet.base.org"
CHAIN_ID = 8453


def connect():
    return Web3(Web3.HTTPProvider(RPC_URL))


def get_account(private_key, w3):
    return w3.eth.account.from_key(private_key)


w3 = connect()

private_key = "YOUR_PRIVATE_KEY"
account = get_account(private_key, w3)

print(f"Connected to Base: {w3.is_connected()}")
print(f"Account: {account.address}")

token = w3.eth.contract(
    address=Web3.to_checksum_address("0xTokenAddress"),
    abi=[{
        "name": "transfer",
        "type": "function",
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ]
    }]
)

tx = token.functions.transfer(
    Web3.to_checksum_address("0xRecipientAddress"),
    1000000
).build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "chainId": CHAIN_ID
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key)

print("Transaction signed successfully.")
print(signed_tx.raw_transaction.hex())
