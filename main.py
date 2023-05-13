# Импорты
import pyautogui
import time


# Функция для вылова рыбы
def move_rod(rod_number, pos_x, pos_y):
    # Если клюнуло
    if not pyautogui.pixel(pos_x, pos_y) == (0, 0, 0):
        # Запускаем таймаут, чтобы проверить, действительно клюнуло
        # или мы перезабрасываем удочку
        time.sleep(0.8)
        # Если действительно клюнуло, начинаем вываживание
        if not pyautogui.pixel(pos_x, pos_y) == (0, 0, 0):
            # Переключаемся на удочку, на которую клюнуло
            pyautogui.press(f"{rod_number}")
            # Пока рыба не выловлена тащим
            while not pyautogui.pixel(701, 426) == (244, 243, 223):
                # Тащим за леску
                pyautogui.keyDown("g")
                # Тащим за удочку
                pyautogui.press("h")
                pyautogui.keyDown("h")
                # Если клюнула большая рыба
                if :
                    # Сбрасываем рыбу
                    pyautogui.press("space")
                    # Перезакидываем удочку
                    pyautogui.press("t")
                    # Завершаем функцию
                    return
            # Если появился экран, что мы вытащили рыбу, закрываем его
            pyautogui.press("space")
            # Перезакидываем удочку
            pyautogui.press("t")
            # Выходим из функции
            return
        # Если мы перезабрасывали удочку
        else:
            # Выходим из функции
            return


# Бесконечный цикл для работы скрипта
while True:
    # Функция для удочки
    move_rod(1, 769, 425)
