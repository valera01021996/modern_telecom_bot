from netmiko import ConnectHandler
import re

mikrotik_router = {
    'device_type': 'mikrotik_routeros',
    'host': "10.10.9.2",
    'port': '22',
    'username': 'for_bot',
    'password': 'txfnUb6Nd8'
}

sshcli = ConnectHandler(**mikrotik_router)

output = sshcli.send_command("ip arp/print where address=10.10.9.1")
pattern = r"(DC)\s+([\d.]+)\s+([0-9A-Fa-f:]+)"
match = re.search(pattern, output)

if match:
    flag = match.group(1)
    address = match.group(2)
    mac_address = match.group(3)
    print("Flag:", flag)
    print("Address:", address)
    print("MAC Address:", mac_address)
else:
    print("Соответствие не найдено.")
