# ----- испорт необходимых модулей ---
import datetime
import time
# ----- создание списков для удобства вывода ----
chapters = ['- Стандартный калькулятор - 1', '- Секундомер - 2']
type_operations = ['- Базовые - 1', '- Продвинутые - 2']
main_operations = ['- Сложение - 1', '- Вычитание - 2', '- Умножение - 3', '- Деление - 4', '- Вычисление остатка - 5', '- Возведение в степень - 6']
advanced_operations = ['Выберите тип операции из списка:',
          '- Конвертер масс - 1', '- Конвертер мер - 2',
          '- Расчет доходности вклада - 3', '- Перевод числа из различных систем счисления в десятичную - 4']
masses = ['- Килограммы - 1', '- Граммы - 2', '- Тонны - 3', '- Центнеры - 4',
              '- Килотонны - 5', '- Миллиграммы - 6']
measures = ['- Метры - 1', '- Километры - 2', '- Миллиметры - 3', '- Сантиметры - 4']
# ----- приветствие пользователя, просьба его выбрать раздел калькулятора и так далее. 
time.sleep(0.5) # -------- использовал метод sleep для плавности вывода -------------------------------------
print('Добро пожаловать в Калькулятор 2.0 ! ✨')
time.sleep(0.5)
print('При выборе операций указывайте только номер операции ❗')
time.sleep(0.5)
print('Вы так же можете вернуться к началу что бы заново выбрать раздел, тип операции и так далее ❗')
time.sleep(0.5)
print('Для этого достаточно ввести слово "назад" при вводе в операции. Для остановки всей программы введите "стоп" ! ')
time.sleep(1)
# ---------------------------------------------------------------------------------------------------------------------------

# --------- старт программы -------------
def start(): # использовал функции что бы можно было вернуться к определенным частям кода -- 
    print('Что вас интересует ?')
    for i in chapters:
        time.sleep(0.9) # из модуля time использовал метод sleep для более плавного вывода ---
        print(i)
    try: # добавил обработки ошибок в коде, если ошибка есть - пользователя вернет в начало ---
        charter = int(input('> '))
    except ValueError:
        print('Ошибка ввода ❗ Возвращение в начало...')
        time.sleep(2)
        start()
    chapteronetwo(charter) # вызываю функцию chapteronetwo и передаю туда выбор пользователя в переменной  -- 


def chapteronetwo(charter): # основная функция 
    import time
    if charter == 1:
        print('Выберите тип математических операций !')
        for i in type_operations:
            time.sleep(0.9)
            print(i)
        try:
            operation = int(input('> '))
        except ValueError:
            print('Ошибка ввода ❗ Возвращение в начало...')
            time.sleep(2)
            start()
        if operation == 1:
            print(' Вы находитесь в базовых операциях ! Выберите операцию из списка доступных 📄')
            for i in main_operations:
                time.sleep(0.4)
                print(i)
            try:
                choice_operation = int(input('> '))
            except ValueError:
                print('Ошибка ввода ❗ Возвращение в начало...')
                time.sleep(2)
                start()

        
            if choice_operation == 1:
                while True:
                    try:
                        num_1 = input('Введите первое число: ')
                        if num_1 == 'назад':
                            start()
                            break
                        if num_1 == 'стоп':
                            break
                        num_2 = input('Введите второе число: ')
                        if num_2 == 'назад':
                            start()
                            break
                        if num_2 == 'стоп':
                            break
                        print('Результат = ', int(num_1) + int(num_2)) # сложение
                    except ValueError:
                                print('Ошибка ввода ❗ Возвращение в начало...')
                                time.sleep(2)
                                start()
                                break 

        

            if choice_operation == 2:
                while True:
                    try:
                        num_1 = input('Введите первое число: ')
                        if num_1 == 'назад':
                            start()
                            break
                        if num_1 == 'стоп':
                            break
                        num_2 = input('Введите второе число: ')
                        if num_2 == 'назад':
                            start()
                            break
                        if num_2 == 'стоп':
                            break
                        print('Результат = ', int(num_1) - int(num_2)) # вычитание
                    except ValueError:
                                print('Ошибка ввода ❗ Возвращение в начало...')
                                time.sleep(2)
                                start()
                                break 



            if choice_operation == 3:
                    while True:
                            try:
                                num_1 = input('Введите первое число: ')
                                if num_1 == 'назад':
                                    start()
                                    break
                                if num_1 == 'стоп':
                                    break
                                num_2 = input('Введите второе число: ')
                                if num_2 == 'назад':
                                    start()
                                    break
                                if num_2 == 'стоп':
                                    break                            
                                print('Результат = ', int(num_1) * int(num_2)) # умножение
                            except ValueError:
                                print('Ошибка ввода ❗ Возвращение в начало...')
                                time.sleep(2)
                                start()
                                break 

        
            if choice_operation == 4:
                    while True:
                        num_1 = input('Введите первое число: ')
                        if num_1 == 'назад':
                            start()
                            break
                        if num_1 == 'стоп':
                            break
                        num_2 = input('Введите второе число: ')
                        if num_2 == 'назад':
                            start()
                            break
                        if num_2 == 'стоп':
                            break
                        print('- Целочисленное - 1', '- С остатком - 2', sep='\n')
                        choice_subtype = int(input('> '))
                        try:
                            if choice_subtype == 1:
                                print('Результат = ', int(num_1) // int(num_2))  # Целочисленное деление.
                            else:
                                print('Результат = ', int(num_1) / int(num_2)) # Деление с остатком 
                        except ZeroDivisionError:
                            print('Ошибка ❗ Деление на 0 невозможно. Возвращение в начало..')
                            time.sleep(1)
                            start()
                        except ValueError:
                            print('Ошибка ❗ Скорее всего где надо ввести цифры, вы ввелите буквы. В начало...')
                            time.sleep(1.5)
                            start()

            if choice_operation == 5:
                while True:
                    try:
                        num_1 = input('Введите первое число: ')
                        if num_1 == 'назад':
                            start()
                            break
                        if num_1 == 'стоп':
                            break
                        num_2 = input('Введите второе число: ')
                        if num_2 == 'назад':
                            start()
                            break
                        if num_2 == 'стоп':
                            break
                        if int(num_1) % int(num_2) == 0:
                            print('Остатка нет!')
                        else:
                            print('Результат = ', int(num_1) % int(num_2)) # остаток от деления
                    except ValueError:
                                print('Ошибка ввода ❗ Возвращение в начало...')
                                time.sleep(2)
                                start()
                                break 


                
            if choice_operation == 6:
                while True:
                    try:
                        num_1 = input('Введите число: ')
                        if num_1 == 'назад':
                            start()
                            break
                        if num_1 == 'стоп':
                            break
                        num_2 = input('Введите степень: ')
                        if num_2 == 'назад':
                            start()
                            break
                        if num_2 == 'стоп':
                            break
                        print(f'Число {num_1} в степени {num_2} = {int(num_1) ** int(num_2)}') # возведение в степень
                    except ValueError:
                                print('Ошибка ввода ❗ Возвращение в начало...')
                                time.sleep(2)
                                start()
                                break 



        if operation == 2:
            print('Вы находитесь в продвинутых операциях ! Выберите нужную операцию из списка доступных 📄')
            for i in advanced_operations:
                time.sleep(0.4)
                print(i)
            choice_operation = int(input('> '))

            if choice_operation == 1:
                while True:
                    try:
                        time.sleep(0.7)
                        print('Из какой массы конвертируем?')
                        for i in masses:
                            time.sleep(0.4)
                            print(i)
                        initial_mer = input('> ')

                        if initial_mer == 'назад':
                            start()
                            break
                        if initial_mer == 'стоп':
                            break 

                        print('В какую массу конвертируем?')
                        for i in masses:
                            time.sleep(0.4)
                            print(i)
                        final_mer = input('> ')


                        if final_mer == 'назад':
                            start()
                            break
                        if final_mer == 'стоп':
                            break  

                        x_mer = input('Введите значение исходной массы: ')

                        if x_mer == 'назад':
                            start()
                            break
                        if x_mer == 'стоп':
                            break  
                        # --------------------------------------------------------------------------------------
                        # ГРАММЫ ------------------------------------------------------------------------------
                        if initial_mer == '2' and final_mer == '1':
                            print(int(int(x_mer)) / 1000, end='кг\n')
                        elif initial_mer == '2' and initial_mer == '4':
                            print(int(int(x_mer)) / 100000, end='цн\n')
                        elif initial_mer == '2' and initial_mer == '3':
                            print(int(int(x_mer)) / 1000000, end='тонн\n')
                        elif initial_mer == '2' and initial_mer == '5':
                            print(int(int(x_mer)) / 1000000000, end='кт\n')
                        elif initial_mer == '2' and initial_mer == '6':
                            print(int(int(x_mer)) * 1000, end='мг\n')
                        # КИЛОГРАММЫ ------------------------------------------------------------------------
                        elif initial_mer == '1' and final_mer == '2':
                            print(int(int(x_mer)) * 1000, end='гр\n')
                        elif initial_mer == '1' and initial_mer == '3':
                            print(int(int(x_mer)) / 1000, end='тонн\n')
                        elif initial_mer == '1' and initial_mer == '5':
                            print(int(int(x_mer)) / 1000000, end='кт\n')
                        elif initial_mer == '1' and initial_mer == '6':
                            print(int(int(x_mer)) * 1000000, end='мг\n')
                        elif initial_mer == '1' and initial_mer == '4':
                            print(int(int(x_mer)) * 100, end='цт\n')
                        # ТОННЫ ------------------------------------------------------------------------------
                        elif initial_mer == '3' and final_mer == '2':
                            print(int(int(x_mer)) * 1000000, end='гр\n')
                        elif initial_mer == '3' and final_mer == '1':
                            print(int(int(x_mer)) * 1000, end='кг\n')
                        elif initial_mer == '3' and initial_mer == '5':
                            print(int(int(x_mer)) * 0.001, end='кт\n')
                        elif initial_mer == '3' and initial_mer == '6':
                            print(int(int(x_mer)) * 1000000000, end='мг\n')
                        elif initial_mer == '3' and initial_mer == '4':
                            print(int(int(x_mer)) * 10, end='цт\n')
                        # ЦЕНТНЕРЫ --------------------------------------------------------------------------------
                        elif initial_mer == '4' and final_mer == '2':
                            print(int(int(x_mer)) * 1000000, end='гр\n')
                        elif initial_mer == '4' and final_mer == '1':
                            print(int(int(x_mer)) * 100, end='кг\n')
                        elif initial_mer == '4' and initial_mer == '5':
                            print(int(int(x_mer)) * 0.0001, end='кт\n')
                        elif initial_mer == '4' and initial_mer == '6':
                            print(int(int(x_mer)) * 100000000, end='мг\n')
                        elif initial_mer == '4' and initial_mer == '3':
                            print(int(int(x_mer)) * 0.01, end='тонн\n')
                        # КИЛОТОННЫ ------------------------------------------------------------------------------
                        elif initial_mer == '5' and final_mer == '2':
                            print(int(int(x_mer)) * 1000000000, end='гр\n')
                        elif initial_mer == '5' and final_mer == '1':
                            print(int(int(x_mer)) * 1000000, end='кг\n')
                        elif initial_mer == '5' and initial_mer == '4':
                            print(int(int(x_mer)) * 10000, end='цн\n')
                        elif initial_mer == '5' and initial_mer == '6':
                            print(int(int(x_mer)) * 1000000000000, end='мг\n')
                        elif initial_mer == '5' and initial_mer == '3':
                            print(int(int(x_mer)) * 1000, end='тонн\n')
                        # МИЛЛИГРАММЫ -----------------------------------------------------------------------------
                        elif initial_mer == '6' and final_mer == '2':
                            print(int(int(x_mer)) * 0.001, end='гр\n')
                        elif initial_mer == '6' and final_mer == '1':
                            print(int(int(x_mer)) * 0.000001, end='кг\n')
                        elif initial_mer == '6' and initial_mer == '4':
                            print(int(int(x_mer)) * 0.00000001, end='цн\n')
                        elif initial_mer == '6' and initial_mer == '5':
                            print(int(int(x_mer)) * 0.000000000001, end='кт\n')
                        elif initial_mer == '6' and initial_mer == '3':
                            print(int(int(x_mer)) * 0.000000001, end='тонн\n')
                    except ValueError:
                        print('Ошибка ввода ❗ Возвращение в начало...')
                        time.sleep(2)
                        start()
                        break 

            
            if choice_operation == 2:
                while True:
                    try:
                        time.sleep(0.7)
                        print('Из какой меры конвертируем?')
                        for i in measures:
                            time.sleep(0.4)
                            print(i)
                        initial_mer = input('> ')
                        if initial_mer == 'назад':
                            start()
                            break
                        if initial_mer == 'стоп':
                            break 
                        print('В какую меру конвертируем?')
                        for i in measures:
                            time.sleep(0.4)
                            print(i)
                        final_mer = input('> ')
                        if final_mer == 'назад':
                            start()
                            break
                        if final_mer == 'стоп':
                            break  
                        x_mer = input('Введите значение исходной меры: ')
                        if x_mer == 'назад':
                            start()
                            break
                        if x_mer == 'стоп':
                            break 
                        # МЕТРЫ | Ниже перевод из значения исходной меры в значение другой меры. ---------
                        if initial_mer == '1' and final_mer == '2':
                            print(int(x_mer) / 1000, end='км\n')
                        elif initial_mer == '1' and final_mer == '3':
                            print(int(x_mer) * 1000, end='мл\n')
                        elif initial_mer == '1' and final_mer == '4':
                            print(int(x_mer) * 100, end='см\n')
                        # САНТИМЕТРЫ ------------------------------------------------------------------
                        if initial_mer == '4' and final_mer == '2':
                            print(int(x_mer) * 0.00001, end='км\n')
                        elif initial_mer == '4' and final_mer == '3':
                            print(int(x_mer) * 10, end='мл\n')
                        elif initial_mer == '4' and final_mer == '1':
                            print(int(x_mer) * 0.01, end='м\n')
                        # МИЛЛИМЕТРЫ ----------------------------------------------------------------------
                        if initial_mer == '3' and final_mer == '2':
                            print(int(x_mer) * 0.000001, end='км\n')
                        elif initial_mer == '3' and final_mer == '4':
                            print(int(x_mer) * 0.1, end='см\n')
                        elif initial_mer == '3' and final_mer == '1':
                            print(int(x_mer) * 0.001, end='м\n')
                        # КИЛОМЕТРЫ ------------------------------------------------------------------------------
                        if initial_mer == '2' and final_mer == '3':
                            print(int(x_mer) * 1000000, end='мл\n')
                        elif initial_mer == '2' and final_mer == '4':
                            print(int(x_mer) * 1000, end='см\n')
                        elif initial_mer == '2' and final_mer == '1':
                            print(int(x_mer) * 100, end='м\n') 
                    except ValueError:
                        print('Ошибка ввода ❗ Возвращение в начало...')
                        time.sleep(2)
                        start()
                        break 


            if choice_operation == 3:
                while True:
                    try:
                        principal = input("Введите сумму вклада: ")
                        if principal == 'назад':
                            start()
                            break
                        if principal == 'стоп':
                            break
                        rate = input("Введите годовую процентную ставку (%): ")
                        if rate == 'назад':
                            start()
                            break
                        if rate == 'стоп':
                            break
                        time = input("Введите срок вклада (в годах): ")
                        if time == 'назад':
                            start()
                            break
                        if time == 'стоп':
                            break

                        # Расчет доходности вклада
                        interest = (int(principal) * int(rate) * int(time)) // 100

                        # Расчет общей суммы с процентами
                        total_amount = int(principal) + int(interest)

                        # Вывод результатов
                        print("Доходность вклада:", interest)
                        print("Общая сумма с процентами:", total_amount)
                    except ValueError:
                        print('Ошибка ввода ❗ Возвращение в начало...')
                        time.sleep(2)
                        start()
                        break 
                    except AttributeError:
                        print('Неверный формат данных ⚠️ Возвращение в начало...')
                        time.sleep(2)
                        start()
                        break


            if choice_operation == 4:
                while True:
                    try:
                        number = input("Введите число: ")
                        if number == 'назад':
                            start()
                            break
                        if number == 'стоп':
                            break  # вводим число
                        base = input("Введите систему счисления числа: ")
                        if base == 'назад':
                            start()
                            break
                        if base == 'стоп':
                            break 
                        if base <= 1:  
                            print('Система счисления может быть только от 2-ух и до 36!')
                        else:
                            
                            decimal_number = int(number, int(base))  
                            
                            print("Число в десятичной системе счисления:", decimal_number)
                    except ValueError:
                        print('Ошибка ввода ❗ Возвращение в начало...')
                        time.sleep(2)
                        start()
                        break 
                    except TypeError:
                        print('Ошибка типа данных 🙅‍♂️ Возвращение в начало...')
                        time.sleep(2)
                        start()
                        break
    if charter == 2:
        import stopwatch
        stopwatch.greet()

start()
 
# весь стандартный калькулятор --------------------------------------------------------------------------------------------
