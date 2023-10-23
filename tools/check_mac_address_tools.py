from .utils import connect_to_router
import re

def check_availability_mac_address(ip_address):
    sshcli = connect_to_router("10.10.9.2")
    output = sshcli.send_command(f"ip arp/print where address={ip_address}")
    pattern = r"(DC)\s+([\d.]+)\s+([0-9A-Fa-f:]+)"
    match = re.search(pattern, output)
    if match:
        flag = match.group(1)
        address = match.group(2)
        mac_address = match.group(3)
        # print("Flag:", flag)
        # print("Address:", address)
        # print("MAC Address:", mac_address)
        return f"✅Flag: {flag} \n" \
               f"Address: {address}\n" \
               f"MAC Address: {mac_address}"
    else:
        # print("Соответствие не найдено.")
        return "Соответствие не найдено."
