def sign_tx(w3, tx, key):
    return w3.eth.account.sign_transaction(tx, key)
