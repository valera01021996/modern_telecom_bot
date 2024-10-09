# from .utils import connect_to_router
# import re
#
# def check_availability_mac_address(ip_address):
#     sshcli = connect_to_router("192.168.100.1")
#     output = sshcli.send_command_timing(f"ip arp print where address={ip_address}")
#     pattern = r"(DC)\s+([\d.]+)\s+([0-9A-Fa-f:]+)"
#     match = re.search(pattern, output)
#     if match:
#         flag = match.group(1)
#         address = match.group(2)
#         mac_address = match.group(3)
#         return f"✅Flag: {flag} \n" \
#                f"Address: {address}\n" \
#                f"MAC Address: {mac_address}"
#     else:
#         return "❗ Соответствие не найдено."

from routeros_api import RouterOsApiPool


def check_arp_entry(ip_address):
    host = '192.168.100.1'
    username = 'for_bot'
    password = 'txfnUb6Nd8'
    connection = RouterOsApiPool(host, username=username, password=password, plaintext_login=True)
    api = connection.get_api()

    # Получаем ресурс ARP
    arp_resource = api.get_resource('/ip/arp')

    # Проверяем наличие записи ARP по IP-адресу
    arp_entries = arp_resource.get(address=ip_address)

    if arp_entries:
        for entry in arp_entries:
            mac_address = entry.get('mac-address', 'N/A')
            interface = entry.get('interface', 'N/A')
            connection.disconnect()
            return f"✅ IP: {ip_address} найден в ARP. \nMAC Address: {mac_address} \nInterface: {interface}"
    else:
        connection.disconnect()
        return f"❗ IP: {ip_address} не найден в ARP."


# Пример вызова функции
result = check_arp_entry('192.168.100.5')
print(result)
