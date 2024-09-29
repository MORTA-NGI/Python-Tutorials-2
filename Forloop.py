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
for c in range(2):
    no1=int(input('Enter the first number '))
    no2=int(input('Enter the second number '))


    print("divition " , div(no1,no2))
    print(" sum ", sum(no1,no2))
    print("subtaction" , sub(no1,no2))
    print("muliplacation " , multi(no1,no2))