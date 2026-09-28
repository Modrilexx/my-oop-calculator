from calculator.calculation import Add, Subtract
from calculator.history import History


def run():
    history = History()

    print("Calculator")
    print("Type 'help' to see commands.")

    while True:
        command = input("> ").strip().lower()

        if command == "add":
            first = float(input("First number: "))
            second = float(input("Second number: "))

            calculation = Add(first, second)
            history.add(calculation)

            print(f"Result: {calculation.get_result()}")

        elif command == "subtract":
            first = float(input("First number: "))
            second = float(input("Second number: "))

            calculation = Subtract(first, second)
            history.add(calculation)

            print(f"Result: {calculation.get_result()}")

        elif command == "history":
            print("Calculation History")

            calculations = history.get_all()

            if not calculations:
                print("No calculations yet.")
            else:
                for index, calculation in enumerate(calculations, start=1):
                    name = calculation.__class__.__name__
                    print(
                        f"{index}. {name}: "
                        f"{calculation.a}, {calculation.b} "
                        f"= {calculation.get_result()}"
                    )

        elif command == "remove":
            number = int(input("Calculation number: "))
            history.remove(number - 1)
            print("Calculation removed.")

        elif command == "help":
            print("Commands: add, subtract, history, remove, help, exit")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")