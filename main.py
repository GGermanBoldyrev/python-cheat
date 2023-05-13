# Импорты
import pyautogui
import time


# Функция для вылова рыбы
def move_rod(rod_number, pos_x):
    # Если клюнуло
    if not pyautogui.pixel(pos_x, 433) == (0, 0, 0):
        # Запускаем таймаут, чтобы проверить, действительно клюнуло
        # или мы перезабрасываем удочку
        time.sleep(0.8)
        # Если действительно клюнуло, начинаем вываживание
        if not pyautogui.pixel(pos_x, 433) == (0, 0, 0):
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
                if pyautogui.pixel(996, 721) == (196, 175, 47):
                    # Отжимаем все кнопки
                    pyautogui.keyUp("g")
                    pyautogui.keyUp("h")
                    # Сбрасываем рыбу
                    pyautogui.press("space")
                    # Перезакидываем удочку
                    pyautogui.press("t")
                    # Завершаем функцию
                    return
            # Если появился экран, что мы вытащили рыбу
            # Пробуем сделать наживку
            with pyautogui.hold('shift'):
                pyautogui.press("b")
            # Таймаут, если выскочит окно, что нельзя сделать наживку
            time.sleep(0.18)
            # Закрываем окно
            pyautogui.press("space")
            # На всякий случай ставим еще один таймаут
            time.sleep(0.05)
            # Проверяем нет ли окна, что нельзя сделать наживку
            if pyautogui.pixel(969, 541) == (244, 243, 223):
                pyautogui.press("space")
            # Перезакидываем удочку
            pyautogui.press("t")
            # Выходим из функции
            return
        # Если мы перезабрасывали удочку
        else:
            # Выходим из функции
            return


# Функция автоматической еды
def eat():
    if pyautogui.pixel(474, 780) == (215, 220, 198):
        pyautogui.click(x=627, y=834)
        time.sleep(1)
        pyautogui.doubleClick(x=784, y=575)
        time.sleep(0.25)
        pyautogui.press("space")
        return


# Бесконечный цикл для работы скрипта
while True:
    # Функция для еды
    eat()
    # Функция для удочки
   # move_rod(1, 951)
    #move_rod(2, 997)
   # move_rod(3, 1009)
