def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divid(x, y):
    if y != 0:
        return x / y
    else:
        return "Fejl: Division med nul!"

def main():
    print("Vælg operation:")
    print("1.Addition")
    print("2.Subtraktion")
    print("3.Multiplikation")
    print("4.Division")

    choice = input("Indtast valg(1/2/3/4): ")
    num1 = float(input("Indtast første tal: "))
    num2 = float(input("Indtast anden tal: "))

    if choice == '1':
        print(f"{num1}+{num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1}-{num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1}*{num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1}/{num2} = {divid(num1, num2)}")
    else:
        print("Ugyldigt valg")

if __name__ == "__main__":
    main()
