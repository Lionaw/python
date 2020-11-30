#20201112 &Lionaw

def Collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3*number +1
    print(number)
    return number

number = int(input("请输入一个数字："))
while number != 1:
    number=Collatz(number)
