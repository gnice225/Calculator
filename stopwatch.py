import time
import keyboard

def greet():
    print("Секундомер 🕓")
    print('В данной программе вы сможете засекать время!')
    print('Нажмите клавишу F для запуска секундомера. Для остановки нажмите S. Для выхода нажмите H.')
    while True:
        if keyboard.is_pressed('F'):
            sec()
        if keyboard.is_pressed('H'):
            break


def sec(): # основная функция
    start = time.time()
    print("Секундомер запущен!")
    while True:
        if keyboard.is_pressed('S'):
            end = time.time()
            elapsed_time = end - start
            print(f"\nСекундомер остановлен! Прошло {format_time(elapsed_time)}.")
            break
        else:
            elapsed_time = time.time() - start
            print(f"Прошло {format_time(elapsed_time)}", end="\r", flush=True)

def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:.2f}"


greet()