inte = int(input())
num = (((inte*2+0.25)**0.5)-0.5)
num1 = int(((inte*2+0.25)**0.5)-0.5)
num2 = int((((int(((inte*2+0.25)**0.5)-0.5)+0.5)**2)-0.25)/2)
if(num == num1):
    if num1 % 2 == 0:
        print(str(num1)+"/1")
    else:
        print("1/"+str(num1))
else:
    check = num1+2
    if num1 % 2 == 0:
        print(str(check-inte+num2)+"/"+str(inte-num2))
    else:
        print(str(inte-num2)+"/"+str(check-inte+num2))