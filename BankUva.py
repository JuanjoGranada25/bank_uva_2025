balance = 0
history = []

def register_movement(current_balance, current_history):
    motive = input("Motive: ")
    type_movement = input("Type (income/expense): ").lower()
    amount_str = input("Amount: ")
    amount = float(amount_str)
    if type_movement == "expense":
        amount = -amount
    elif type_movement != "income":
        print("Invalid movement type. Assuming income.")

    movement = {"motive": motive, "amount": amount, "type": type_movement}
    new_history = current_history + [movement]
    new_balance = current_balance + amount
    print("Movement registered. New balance:", new_balance)
    return new_balance, new_history

def show_history(current_history, current_balance):
    print("Movement History:")
    if not current_history:
        print("No movements yet.")
        return
    for move in current_history:
        print(f"{move['motive']} ({move['type']}):", move['amount'])
    print("Current Balance:", current_balance)

def show_balance(current_balance):
    print("Current Balance:", current_balance)

def main():
    current_balance = balance
    current_history = history
    while True:
        print("BankUva Manager")
        print("Balance:", current_balance)
        print("1. Register Movement")
        print("2. Show History")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Select option: ")
        if choice == '1':
            current_balance, current_history = register_movement(current_balance, current_history)
        elif choice == '2':
            show_history(current_history, current_balance)
        elif choice == '3':
            show_balance(current_balance)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

    return current_balance, current_history

final_balance, final_history = main()
balance = final_balance
history = final_history
print("Final Balance:", balance)
print("Final History:", history)

main()