def get_balance(address, w3):
    balance = w3.eth.get_balance(address)
    return w3.from_wei(balance, "ether")


print(f"Balance: {get_balance(account.address, w3)} ETH")
