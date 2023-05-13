# Импорты
import pyautogui
from pynput import mouse


# Функция для поиска цвета и позиции удочки на экране
def get_pos_and_color():
    # Позиция курсора
    position = pyautogui.position()
    # Цвет пикселя
    color = pyautogui.pixel(position.x, position.y)
    # Выводим найденные значения в консоль
    print(position)
    print(color)


# Функция на клик по левой кнопке мышки
def on_click(x, y, button, pressed):
    # Выводим значения цвета и позиции курсора
    get_pos_and_color()


# Запускаем процесс
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
