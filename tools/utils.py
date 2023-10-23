from netmiko import ConnectHandler

def connect_to_router(host: str):
    mikrotik_router = {
        'device_type': 'mikrotik_routeros',
        'host': host,
        'port': '22',
        'username': 'for_bot',
        'password': 'txfnUb6Nd8'
    }
    sshCli = ConnectHandler(**mikrotik_router)
    return sshCli