'''
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

namber=int(input('Введите 3-х значное число '))
sum=namber//100+namber//10%10+namber%10
print(f'Сумма цифр {namber} = {sum}')