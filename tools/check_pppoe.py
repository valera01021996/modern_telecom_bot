from routeros_api import RouterOsApiPool


def check_pppoe_session(name):
    host = '192.168.100.1'
    username = 'for_bot'
    password = 'txfnUb6Nd8'
    connection = RouterOsApiPool(host, username=username, password=password, plaintext_login=True)
    api = connection.get_api()

    ppp_active = api.get_resource('/ppp/active')
    active_sessions = ppp_active.get()

    for session in active_sessions:
        if session.get('name') == name:
            connection.disconnect()
            return f"PPPoe session on interface {name} is active.✅"

    connection.disconnect()
    return f"No active PPPoe session found on interface {name}.🚫"



