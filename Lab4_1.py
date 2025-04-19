import random
from datetime import datetime
num = random.randint(1,101)
user = int(input('Напишите число: '))
count = 1
current_date = datetime.now()
for i in range(3):
    if user == num:
        print('Вы правильно угадали число', num, '.', 'Попытки: ', count, '.', 'Время', current_date)
        break
    if user > num:
        print('Число больше заданного', 'Время', current_date)
        count += 1
        user = int(input('Напишите число: '))
    if user < num:
        print('Число меньше заданного', 'Время', current_date)
        count += 1
        user = int(input('Напишите число: '))
    if count == 10:
        print('Попытки закончились! Заданное число', num, '.', 'Попытки: ', count, '.', 'Время', current_date)
        break