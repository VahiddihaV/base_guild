from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.base.org"))

private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)

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
    "chainId": 8453
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
print(signed_tx.raw_transaction.hex())
