def safe_to_checksum(w3, addr):
    try:
        return w3.to_checksum_address(addr)
    except:
        return None
