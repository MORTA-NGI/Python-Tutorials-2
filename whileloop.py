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
try:
    while True:
        no1=int(input('Enter the first number '))
        no2=int(input('Enter the second number '))
        if no2>0:
            print("divition " , div(no1,no2))
        else:
            print("The sum is: ", sum(no1,no2))
            print("The subtaction is:" , sub(no1,no2))
            print("The muliplacation is: " , multi(no1,no2))
except TypeError:
    print('typeError')
except ZeroDivisionError:
    print('typeError')
except:
    print('typeError')
    