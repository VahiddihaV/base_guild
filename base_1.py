def load_account(w3, private_key):
    return w3.eth.account.from_key(private_key)
