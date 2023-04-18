#Определение знака зодиака по дате рождения

birth_month = input('Введите месяц: ')
birth_day = int(input('Введите число: '))
zodiac_sing = ''

if birth_month == 'март' and 21 <= birth_day <= 31 or birth_month == 'апрель' and 1 <= birth_day <= 19:
    zodiac_sing = 'Овен'
if birth_month == 'апрель' and 20 <= birth_day <= 30 or birth_month == 'май' and 1 <= birth_day <= 20:
    zodiac_sing = 'Телец'
if birth_month == 'май' and 21 <= birth_day <= 31 or birth_month == 'июнь' and 1 <= birth_day <= 20:
    zodiac_sing = 'Близнецы'
if birth_month == 'июнь' and 21 <= birth_day <= 30 or birth_month == 'июль' and 1 <= birth_day <= 22:
    zodiac_sing = 'Рак'
if birth_month == 'июль' and 23 <= birth_day <= 31 or birth_month == 'август' and 1 <= birth_day <= 22:
    zodiac_sing = 'Лев'
if birth_month == 'август' and 23 <= birth_day <= 31 or birth_month == 'сентябрь' and 1 <= birth_day <= 22:
    zodiac_sing = 'Дева'
if birth_month == 'сентябрь' and 23 <= birth_day <= 30 or birth_month == 'октябрь' and 1 <= birth_day <= 22:
    zodiac_sing = 'Весы'
if birth_month == 'октябрь' and 23 <= birth_day <= 31 or birth_month == 'ноябрь' and 1 <= birth_day <= 21:
    zodiac_sing = 'Скорпион'
if birth_month == 'ноябрь' and 22 <= birth_day <= 30 or birth_month == 'декабрь' and 1 <= birth_day <= 21:
    zodiac_sing = 'Стрелец'
if birth_month == 'декабрь' and 22 <= birth_day <= 31 or birth_month == 'январь' and 1 <= birth_day <= 19:
    zodiac_sing = 'Козерог'
if birth_month == 'январь' and 20 <= birth_day <= 31 or birth_month == 'февраль' and 1 <= birth_day <= 18:
    zodiac_sing = 'Водолей'
if birth_month == 'февраль' and 21 <= birth_day <= 28 or birth_month == 'март' and 1 <= birth_day <= 20:
    zodiac_sing = 'Рыбы'

print(f'\nВывод:\n{zodiac_sing}')