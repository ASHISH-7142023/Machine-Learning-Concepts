num=int(input("enter a number: "))
n=num
s=0
if n<0: 
    n=-n
while n>0:
    d=n%10
    s=s+d
    n=n//10
print("Sum of digits: "+s)