def stickerStats(stats) -> list:  # Определяем стикер для статистики
    img = ['Error'] * 3
    stats = list(stats)

    if stats[0] >= 90: img[0] = '🫀' # Стикер для здоровья
    elif stats[0] >= 75: img[0] = '💊'
    elif stats[0] >= 50: img[0] = '🌡'
    elif stats[0] < 50: img[0] = '🦠'

    if stats[4] <= 1: img[1] = '🚂' # Стикер для скорости
    elif stats[4] <= 2: img[1] = '🚈'
    elif stats[4] <= 3: img[1] = '🚅'
    elif stats[4] >= 4: img[1] = '🚄'

    if stats[5] <= 150: img[2] = '🧸' # Стикер для опыта
    elif stats[5] <= 500: img[2] = '📦'
    elif stats[5] <= 1000: img[2] = '📈'
    elif stats[5] >= 2000: img[2] = '💯'

    return img
