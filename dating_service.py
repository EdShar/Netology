#Сервис знакомств

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Идеальные пары:')

    for boy, girl in zip(sorted(boys), sorted(girls)):
        print(f'{boy} и {girl}')
else:
    print('Знакомства не будет - кто-то останется без пары :(')