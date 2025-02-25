def add(n1,n2):
    return n1+n2
def subtrct(n1,n2):
    return n1-n2
def division(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
print("1 is for addition")
print("2 is for Subtraction")
print("3 is for Division")
print("4 is for Multiplication")
i=int(input("Enter any number from 1 to 4 \n"))
n1=float(input("Enter the number1 :"))
n2=float(input("Enter the number2 :"))
if(i==1):
    print(n1,"+",n2,"=",n1+n2)
elif(i==2):
    print(n1,"-",n2,"=",n1-n2)
elif(i==3):
    print(n1,"/",n2,"=",n1/n2)
elif(i==4):
    print(n1,"*",n2,"=",n1*n2)
else:
    print("INVALID")
