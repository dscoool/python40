import uuid

def getMacAddress():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

mac_address = getMacAddress()
print(f"MAC Address: {mac_address}")
