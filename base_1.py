def get_tx_receipt(w3, tx_hash):
    return w3.eth.wait_for_transaction_receipt(tx_hash)
