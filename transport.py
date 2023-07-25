pers = input('year of birth')
dictprice = {
    '90 minutes':   60,
    '7 days':      300,
    '30 days':    1000,
    '365 days':  10000}
pers = int(pers)
age = 2023 - pers
if age < 14 or age > 50:
    print('wihout payment')
elif 14 < age < 24:
    print('cost for 14 < age < 24: ', end =  '')
    for v in dictprice:
        print(v, dictprice[v] / 2, end = ', ') 
else:
    for v in dictprice:
        print(v, dictprice[v])