# Написать программу, которая спрашивает возраст, выбрасывает исключение, 
#если введенное число отрицательное, в противном случае считает год рождения.
import datetime

actualYear = datetime.date.today().year

age = int(input('Сколько тебе лет? '))
if age < 0:
    raise ValueError(
        'Вы ввели неверное число?')
else:
    print('Год рождения (если у тебя уже был ДР в этом году): ' + str(actualYear - age))
