def sign_transaction(w3, tx, private_key):
    return w3.eth.account.sign_transaction(tx, private_key)
