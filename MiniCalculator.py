from calculator import Calculator

class MiniCalculator(Calculator):
    def __init__(self):
        super().__init__(5, 3)  

# Main program
if __name__ == "__main__":
    # Taking inputs for the main Calculator class
    no1 = int(input("Enter the number 1: "))
    no2 = int(input("Enter the number 2: "))
    sign = input("Enter the operation (+,-,*, or /): ")

    # Create an instance of the Calculator class
    calculator = Calculator(no1, no2)

    # Perform operations using Calculator class
    if sign == '+':
        result = calculator.add()
        print('Result of addition is:', result)
    elif sign == '-':
        result = calculator.subtract()
        print('Result of subtraction is:', result)
    elif sign == '*':
        result = calculator.multiply()
        print('Result of multiplication is:', result)
    elif sign == '/':
        result = calculator.divide()
        print('Result of division is:', result)

    # Perform the same operation using MiniCalculator
    mini_calc = MiniCalculator()  # Create an instance of MiniCalculator

    if sign == '+':
        mini_result = mini_calc.add()
        print(f"MiniCalculator result (5 + 3): {mini_result}")
    elif sign == '-':
        mini_result = mini_calc.subtract()
        print(f"MiniCalculator result (5 - 3): {mini_result}")
    elif sign == '*':
        mini_result = mini_calc.multiply()
        print(f"MiniCalculator result (5 * 3): {mini_result}")
    elif sign == '/':
        mini_result = mini_calc.divide()
        print(f"MiniCalculator result (5 / 3): {mini_result}")
