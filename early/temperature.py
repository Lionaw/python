#Lionaw
tempr_1=input()
if tempr_1[-1] in ['f','F']:
    massage = (eval(tempr_1[0:-1])-32)/1.8
    print("F--C\t{:.2f}C".format(massage))
elif tempr_1[-1] in ['c','C']:
    massage = 1.8*eval(tempr_1[0:-1])+32
    print("C--F\n{:.2f}F".format(massage))
else:
    print("fulse")