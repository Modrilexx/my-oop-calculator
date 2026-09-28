from calculator.calculation import Add, Subtract
from calculator.history import History


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")


def run():
    history = History()

    print("Calculator")
    print("Type 'help' to see commands.")

    while True:
        try:
            command = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if command == "add":
            first = read_number("First number: ")
            second = read_number("Second number: ")

            calculation = Add(first, second)
            history.add(calculation)

            print(f"Result: {calculation.get_result()}")

        elif command == "subtract":
            first = read_number("First number: ")
            second = read_number("Second number: ")

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
            try:
                number = int(input("Calculation number: "))

                if number < 1 or number > history.count():
                    print("Invalid calculation number.")
                    continue

                history.remove(number - 1)
                print("Calculation removed.")

            except ValueError:
                print("Invalid calculation number.")

        elif command == "help":
            print("Commands: add, subtract, history, remove, help, exit")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")