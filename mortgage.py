#Расчет процентной ставки

base_rate = 12

unique_rate = 2
insurance_rate = 1.5
salary_rate = 0.5
children_rate = 1

print('Добро пожаловать в ипотечный калькулятор.')
print('Отвечайте, пожалуйста, на вопросы "Да" или "Нет"\n')

if input('Вы из Дальнего Востока? ') == 'Да':
    base_rate = unique_rate
else:
    if input('У вас есть страхование в нашем банке? ') == 'Да':
        base_rate -= insurance_rate
    if input('У вас есть зарплатный проект в нашем банке? ') == 'Да':
        base_rate -= salary_rate
    if input('У вас больше троих детей? ') == 'Да':
        base_rate -= children_rate

print(f'Ваша финальная процентная ставка = {base_rate} %')