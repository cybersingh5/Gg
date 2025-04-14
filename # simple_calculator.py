# simple_calculator.py

def add(a, b):
    return a + b

def main():
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Sum is:", add(x, y))

if __name__ == "__main__":
    main()
