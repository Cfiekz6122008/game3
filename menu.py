# Пример реализации menu.py (дополните необходимыми функциями)
from tkinter import *
from pickle import load, dump

menu_mode = False
menu_options = ['Возврат в игру', 'Новая игра', 'Сохранить', 'Загрузить', 'Выход']
menu_current_index = 0
menu_options_id = []
pause = False

def menu_create(canvas):
    global menu_options_id
    offest = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(400, 200 + offest, anchor=CENTER, font=('Arial', '25'), text=menu_option, fill='black', tags="menu")
        menu_options_id.append(option_id)
        offest += 50
    menu_update(canvas)

def menu_up(canvas):
    global menu_current_index
    menu_current_index = (menu_current_index - 1) % len(menu_options)
    menu_update(canvas)

def menu_down(canvas):
    global menu_current_index
    menu_current_index = (menu_current_index + 1) % len(menu_options)
    menu_update(canvas)

def menu_update(canvas):
    for idx, option_id in enumerate(menu_options_id):
        if idx == menu_current_index:
            canvas.itemconfig(option_id, fill='blue')
        else:
            canvas.itemconfig(option_id, fill='black')

def menu_enter(canvas):
    global menu_current_index
    if menu_current_index == 0:  # Возврат в игру
        menu_show(canvas)
    elif menu_current_index == 1:  # Новая игра
        start_new_game(canvas)
    elif menu_current_index == 2:  # Сохранить
        game_save()
    elif menu_current_index == 3:  # Загрузить
        game_load(canvas)
    elif menu_current_index == 4:  # Выход
        game_exit()

# Другие функции для управления меню и игрой:
def menu_show(canvas):
    global menu_mode
    menu_mode = True
    canvas.tag_raise("menu")  # Поднять меню над другими элементами


def game_save():
    print('Сохраняем игру')

def game_load(canvas):
    print('Загружаем игру')

def start_new_game(canvas):
    print('Начинаем новую игру')

def game_exit():
    print('Выход из игры')
    exit()
