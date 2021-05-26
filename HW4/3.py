'''
# Я спочатку неправильно зрозумів умову задачі, я подумав, що потрібно ввести число,
# далі перевірити чи воно є числом Фібоначчі і якщо так, то найти наступне число фібоначчі, що йде після нього


n = int(input('Введіть ваше число:'))

list1 = [0,1,2,3,5,8,13,21,34,55,89]


if n in list1:
    print('Ваше число входить до чисел Фібоначчі!')
    if n in list1:
        index = list1.index(n)
        print(f'Наступне число Фібоначчі',{list1[index+1]})

else:
    print('Ваше число не входить до чисел Фібоначчі!')
'''

#Тепер правильне домашнє:)

number_fibonacci = int(input("How many Fibonacci figures do you want?:   "))
num1 = 0
num2 = 1
count = 0
while count < number_fibonacci:
    print(num1,'\n____________')
    final_num = num1 + num2
    num1 = num2
    num2 = final_num
    count +=1

