from datetime import date
today = date.today()

day = int(input('Какой ваш день рождения: '))
month = int(input('Какой месяц вашего рождения: '))
year = int(input('Какой год вашего рождения: '))

age = today.year - year - ((today.month, today.day) < (month, day))

print(f': {age}')
