#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """
        Initialize a Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
            amount (float): The amount to be deposited.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds are available.

        Parameters:
            amount (float): The amount to be withdrawn.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_float(prompt):
    """
    Continuously prompt the user until a valid float is entered.

    Parameters:
        prompt (str): The prompt message to be displayed to the user.

    Returns:
        float: The valid float value entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. Please enter a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function to interact with the user and simulate a checkbook.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = get_valid_float("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_float("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
