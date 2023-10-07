num1=0
num2=1
next_num=num2
n=10
if n==0:
    print(num1)
elif n==1:
    print(num2)
else:
    while n>=0:
        print(next_num, end=' ')
        next_num=num1+num2
        num1=num2
        num2=next_num
        n=n-1


