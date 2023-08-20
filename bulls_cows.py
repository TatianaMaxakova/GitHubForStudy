# Быки и коровы

import random


####### Словоформы

def word_form(n, variants=['год', 'года', 'лет']):
    n = n % 100
    if (n < 5) or (n > 20):  # от 5 до 20 - "стандартный" случай
        if (n % 10) in [2, 3, 4]:
            return variants[1]  # года
        if (n % 10) == 1:
            return variants[0]  # год
    return variants[2] # лет



############ Функуция загадывания числа из неповторяющихся цифр ################

def zagadaika(alphebet='0123456789', word_len=4):  # ARGUMENTS?
    result = ''.join(random.sample(alphebet, word_len))
    return result


def skolko_bykov(chislo, popitka):
    bulls = 0
    for i in range(len(chislo)):
        if chislo[i] == popitka[i]:
            bulls += 1
    return bulls


def skolko_korov(chislo, popitka):
    cows = 0
    for i in range(len(chislo)):
        if popitka[i] in chislo and popitka[i] != chislo[i]:
            cows += 1
    return cows


def main_game():
    chislo = zagadaika()
    print(chislo)
    bylo_popytok = 0
    popitka = ''
    while popitka != chislo:
        bylo_popytok += 1
        popitka = input('Введите 4-х значное число: ')
        if len(popitka) == len(chislo):
            bulls = skolko_bykov(chislo, popitka)
            print(bulls, ' бык' + word_form(bulls, ['' , 'а', 'ов']))  
            cows = skolko_korov(chislo, popitka)
            print(cows, ' коров' + word_form(cows, ['а' , 'ы', '']))  
    return bylo_popytok

    
otvet = 'Да'
while otvet == 'Да':
    tries = main_game()
    print('Угадал за ', tries, ' попыт' + word_form(tries, ['ка' , 'ки', 'ок']) + '!')  
    otvet = input('Сыграем ещё? ')
