def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Sum: {} + {} = {}".format(a,b,a+b))

        elif choice == '2':
            print("Sum: {} - {} = {}".format(a,b,a-b))

        elif choice == '3':
            print("Sum: {} * {} = {}".format(a,b,a*b))

        elif choice == '4':
            print("Sum: {} / {} = {}".format(a,b,a/b))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input") 