def build_erc20_tx(contract, sender, to, amount, w3, chain_id):
    return contract.functions.transfer(
        to,
        amount
    ).build_transaction({
        "from": sender,
        "nonce": w3.eth.get_transaction_count(sender),
        "gas": 100000,
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id
    })
