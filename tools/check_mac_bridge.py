from routeros_api import RouterOsApiPool


def check_mac_in_bridge_hosts(mac_address):
    host = '192.168.100.1'
    username = 'for_bot'
    password = 'txfnUb6Nd8'
    bridge_name = 'bridge-WAN'
    connection = RouterOsApiPool(host, username=username, password=password, plaintext_login=True)
    api = connection.get_api()

    bridge_host_resource = api.get_resource('/interface/bridge/host')
    bridge_hosts = bridge_host_resource.get(bridge=bridge_name)

    for host in bridge_hosts:
        if host.get('mac-address') == mac_address:
            vid = host.get('vid', 'N/A')
            connection.disconnect()
            return f"MAC address {mac_address} is found with VLAN {vid}.✅"

    connection.disconnect()
    return f"MAC address {mac_address} is not found.🚫"

