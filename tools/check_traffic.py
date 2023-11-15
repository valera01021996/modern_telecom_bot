import librouteros
from librouteros.login import plain


def get_traffic_info(ip_address):
    connection = librouteros.connect(
        username='for_bot',
        password='txfnUb6Nd8',
        host='192.168.100.1',
        login_method=plain
    )

    queues = connection.path('/queue/simple')

    text = ""


    for queue in queues.select('target', 'rate'):
        if queue['target'] == ip_address + "/32":
            rate_splitted = queue['rate'].split('/')
            upload = int(rate_splitted[0])/1000000
            download = int(rate_splitted[1])/1000000
            text += f"IP address: {ip_address}\n" \
                    f"Upload: {upload} Мбит/с\n" \
                    f"Download: {download} Мбит/с\n"
        # else:
        #     return "Соответствие не найдено."
    if text:
        return text
    else:
        return "Соответствие не найдено !"

