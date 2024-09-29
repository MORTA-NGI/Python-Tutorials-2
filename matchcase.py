def div(no1, no2):
    div=no1/no2
    return div

def sum(no1, no2):
    div=no1+no2
    return div

def multi(no1, no2):
    div=no1*no2
    return div

def sub(no1, no2):
    div=no1-no2
    return div


no1=int(input('Enter the first number '))
no2=int(input('Enter the second number '))
sign=input("Enter the operation (+,-,*,or /)")

while True: 
    match sign:
        case "+":
            print(sum(no1, no2))
        case "-":
            print(sub(no1, no2))
        case "*":
            print(multi(no1, no2))  
        case "/":
            if no2 >0:
                print(div(no1, no2))
    