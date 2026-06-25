def send_raw_tx(w3, signed_tx):
    return w3.eth.send_raw_transaction(signed_tx.raw_transaction)
