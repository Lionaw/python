""" by lionaw  """
filename = 'pi.txt'
with open(filename,'r',encoding='UTF-8') as file_object:
	contents = file_object.read()
a = input("输入字符并验证：")
while a != 'exit()':
    if a in contents:
	    print("1")
    else:
	    print("2")
    a = input()
