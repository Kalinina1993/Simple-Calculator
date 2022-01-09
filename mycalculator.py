def calc():
    while True:
        print("Select the action you want to make: \n"
              "Add: +\n"
              "Subtract: -\n"
              "Multiply: *\n"
              "Divide: /\n"
              "Exit: q\n")

        action = input("Action: ")
        if action == "q":
            print("program exit")
            break
        if action in ("+", "-", "*", "/"):
            x = float(input("x = "))
            y = float(input("y = "))
        if action == "+":
            print("%.2f + %.2f = %.2f" % (x, y, x + y))
        elif action == "-":
            print("%.2f + %.2f = %.2f" % (x, y, x + y))
        elif action == "*":
            print("%.2f * %.2f = %.2f" % (x, y, x * y))
        elif action == "/":
            if y != 0:
                print("%.2f / %.2f = %.2f" % (x, y, x / y))
            else:
                print("Divide by zero!")


if __name__ == "__main__":
    calc()






