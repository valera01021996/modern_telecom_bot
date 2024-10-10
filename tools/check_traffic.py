import librouteros
from librouteros.login import plain
import matplotlib.pyplot as plt
import io
import matplotlib.patheffects as path_effects

def get_traffic_info(ip_address):
    connection = librouteros.connect(
        username='for_bot',
        password='txfnUb6Nd8',
        host='192.168.100.1',
        login_method=plain
    )

    queues = connection.path('/queue/simple')

    upload = ""
    download = ""
    plt.style.use('ggplot')

    for queue in queues.select('target', 'rate'):
        if queue['target'] == ip_address + "/32":
            rate_splitted = queue['rate'].split('/')
            upload = int(rate_splitted[0]) / 1000000
            download = int(rate_splitted[1]) / 1000000
    fig, ax = plt.subplots()
    bars = ax.bar(['Upload', 'Download'], [upload, download], color=['#1f77b4', '#2ca02c'],
                  edgecolor='black', linewidth=1.5)
    if not upload:
        upload = 0.0
    if not download:
        download = 0.0
        
    # Добавим тени
    for bar in bars:
        bar.set_path_effects([path_effects.SimpleLineShadow(), path_effects.Normal()])

    # Настроим отображение текста
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.2f}', ha='center', va='bottom', fontsize=12,
                color='black')

    # Округленные углы
    for bar in bars:
        bar.set_linestyle('dotted')
        bar.set_linewidth(1.5)

    ax.set_ylabel('Скорость (Мбит/с)', fontsize=12)
    ax.set_title('Текущая скорость', fontsize=16)

    # Установим пределы оси Y
    ax.set_ylim(0, max(float(upload), float(download)) + 10)

    # Сохранение графика в буфер
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    plt.close()

    if buffer:
        return buffer
    else:
        return "Соответствие не найдено !"
