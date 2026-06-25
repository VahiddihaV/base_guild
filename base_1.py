from web3 import Web3

def to_checksum(addr):
    return Web3.to_checksum_address(addr)
