try:
    account = w3.eth.account.from_key(private_key)
except Exception as e:
    logging.error(e)
