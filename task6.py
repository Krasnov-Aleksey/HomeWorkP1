'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''
namTicket=int(input('Введите номер билета '))
sumNam1=namTicket//100000+namTicket//10000%10+namTicket//1000%10
sumNam2=namTicket//100%10+namTicket//10%10+namTicket%10
if sumNam1==sumNam2:
    print('Yes')
else:
    print('No')
