import matplotlib.pyplot as plt
import numpy as np
import requests


def get_data():
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    content = float(response.json()['price'])
    return round(content, 1)


def print_graph():
    plt.style.use('_mpl-gallery')
    start_data = get_data()
    # Инициализируем пустые списки для данных
    y = [start_data]

    # Создаем пустой график
    fig, ax = plt.subplots()

    y_min = max(start_data - 1, 0)
    y_max = start_data + 1
    y_ticks = np.arange(y_min, y_max, 2)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(y_min, y_max), yticks=y_ticks)

    ax.set_xlabel('Time')
    ax.set_ylabel('Price')

    # Главный цикл для динамического рисования элементов
    for i in range(30):
        # Генерируем новое значение для y
        new_value = get_data()
        y.append(new_value)
        print(y)

        # Очищаем предыдущий график и рисуем лестницу с новыми данными
        ax.clear()
        ax.step(range(len(y)), y, where='post', linewidth=2.5)

        # Обновляем график
        plt.draw()
        plt.pause(2)  # Делаем паузу перед следующей итерацией для наглядности

