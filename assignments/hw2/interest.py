"""
Name: <Hugo Bachaumard>
interest.py

Problem: Write a program that determines the monthly interest owed on credit card.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    rate = eval(input("Enter the annual percentage rate."))
    days = eval(input("Enter the number of days in the billing cycle."))
    previous_balance = eval(input("Enter the net balance shown on the statement."))
    payment = eval(input("Enter the net payment received."))
    payment_day = eval(input("Enter the day of the payment."))
    balance_1 = previous_balance * days
    days_before = days - payment_day
    balance_2 = days_before * payment
    balance = balance_1 - balance_2
    average_daily = balance / days
    monthly_interest_rate = (rate / 12) / 100
    monthly_charge = monthly_interest_rate * average_daily
    print(round(monthly_charge, 2))


if __name__ == '__main__':
    main()
