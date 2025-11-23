import csv
import logging
from datetime import datetime


logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# DATA MODEL
class StockTransaction:
    """
    Represents a single stock transaction with calculation features.
    """
    def __init__(self, buy_price, sell_price, quantity, brokerage=0):
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.brokerage = brokerage

    def calculate(self):
        total_cost = (self.buy_price * self.quantity) + self.brokerage
        total_value = (self.sell_price * self.quantity) - self.brokerage
        difference = total_value - total_cost
        percent_change = (difference / total_cost) * 100
        break_even = (total_cost + self.brokerage) / self.quantity

        return {
            "total_cost": total_cost,
            "total_value": total_value,
            "difference": difference,
            "percent_change": percent_change,
            "break_even": break_even
        }


# UTILITY FUNCTIONS 
def get_positive_float(message):
    """
    Safely collects a positive float value from the user.
    """
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter a numeric value.")


def save_transaction(data):
    """
    Saves transaction details to a CSV file.
    """
    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    logging.info("Transaction saved successfully.")


def view_history():
    """
    Displays previously saved transactions.
    """
    try:
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)
            print("\n=== TRANSACTION HISTORY ===")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("\nNo transaction history found.")


# APPLICATION  MAIN
class StockCalculatorApp:
    

    def run(self):
        while True:
            print("\nSTOCK PROFIT/LOSS CALCULATOR")
            print("1. Calculate Profit/Loss")
            print("2. View Transaction History")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.process_transaction()
            elif choice == "2":
                view_history()
            elif choice == "3":
                print("\nThank you for using the calculator!")
                break
            else:
                print("Invalid choice. Try again.")

    def process_transaction(self):
        print("\nENTER TRANSACTION DETAILS")
        buy = get_positive_float("Buy price per share: ₹")
        sell = get_positive_float("Sell price per share: ₹")
        qty = get_positive_float("Number of shares: ")

        include_brokerage = input("Include brokerage? (yes/no): ").lower()
        brokerage = 0

        if include_brokerage == "yes":
            brokerage = get_positive_float("Enter total brokerage: ₹")

        transaction = StockTransaction(buy, sell, qty, brokerage)
        result = transaction.calculate()

        self.display_results(result)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_transaction([
            timestamp, buy, sell, qty, brokerage,
            result["difference"], result["percent_change"]
        ])

    @staticmethod
    def display_results(result):
        print("\nRESULT SUMMARY")
        print(f"Total Cost: ₹{result['total_cost']:.2f}")
        print(f"Total Value: ₹{result['total_value']:.2f}")

        if result["difference"] > 0:
            print(f"Profit: ₹{result['difference']:.2f}")
        elif result["difference"] < 0:
            print(f"Loss: ₹{abs(result['difference']):.2f}")
        else:
            print("➡ No profit, no loss.")

        print(f"Percentage Change: {result['percent_change']:.2f}%")
        print(f"Break-Even Price: ₹{result['break_even']:.2f}")


# RUN APPLICATION
if __name__ == "__main__":
    app = StockCalculatorApp()
    app.run()