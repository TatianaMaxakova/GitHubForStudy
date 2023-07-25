salary = int(input('Ваша ЗП: '))
first_mohth = int(input('Первый месяц (1-12): '))
second_mohth = int(input('Последний месяц (1-12): '))
otpusknye = (second_mohth - first_mohth) * 100 + salary
day = (second_mohth - first_mohth) * 2
print('Ваш отпуск продлится', day, 'дней', отпускные, otpusknye 'рублей')
 