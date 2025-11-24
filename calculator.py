def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return " Error, we can not divide any number by zero, its universal rule."
    return a/b

def nos(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("The number is not valid; Try another one")

def calculate():
    print("Hey, it's your calculator!")

    while True:
        print("1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)")
        print("5: Exit (Thanks!!)")

        choice = input("Enter your choice?!: ")

        if choice == '5':
            print("Thanks! Have a fantastic day! Goodbye! ")
            break
        
        if choice in ('1', '2', '3', '4'):
            a = nos("Enter the First number: ")
            b = nos("Enter the Second number: ")

            result = None
            symbol = ''
            
            if choice == '1':
                result = add(a, b)
                symbol = '+'
                print(f"\nYour Answer {a} {symbol} {b}={result}\n")
            elif choice == '2':
                result = subtract(a, b)
                symbol = '-'
                print(f"\nYour Answer {a} {symbol} {b}={result}\n")
            elif choice == '3':
                result = multiply(a, b)
                symbol = '*'
                print(f"\nYour Answer {a} {symbol} {b}={result}\n")
            elif choice == '4':
                result = divide(a, b)
                symbol = '/'
                print(f"\nYour Answer {a} {symbol} {b}={result}\n")
                
            else:
                result = round(result, 4)
                print(f"\n I've got it! The result of {a} {symbol} {b} is = {result} ")
                print("Wasn't that easy? What's next?")
        
        else:
            print("Please try again by typing (1 , 2 , 3 , 4 , 5)")
if __name__=="__main__":
    calculate()

