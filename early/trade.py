# by lionaw
try:
    print(8/0)
except ZeroDivisionError:
    print("You are stupid")

filename = 'alice.txt'
try:
    with open(filename) as f_obje:
         contents = f_obje.read()
except FileNotFoundError:
    msg = "is error"
    print(msg)

title = 'Alice in Wonderland'
print(title.split())

filename = '11-0.txt'
try:
    with open(filename,encoding='UTF-8') as f_obje:
        contents = f_obje.read()
except FileNotFoundError:
    print("error")
else:
    word = contents.split()
    num_words = len(word)
    print(str(num_words))

def count_words(filename):
    """计算单词数量"""
    try:
        with open(filename, encoding='UTF-8') as f_obje:
            contents = f_obje.read()
    except FileNotFoundError:
        print("error")
    else:
        word = contents.split()
        num_words = len(word)
        print(str(num_words))

filename = '11-0.txt'
count_words(filename)

while True:
    try:
        a = int(input("please input a number: "))
        b = int(input("please input a number: "))
    except TypeError:
        print("Error")
    else:
        c = a+b
        print(c)