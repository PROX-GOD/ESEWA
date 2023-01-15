import os

import webbrowser

def open_facebook():

    webbrowser.open("https://www.facebook.com/")

def get_python_command(command):

    os.system(f"python -c '{command}'")

def copy_python_command():

    my_command = "print('Hello, World!')"

    os.system(f'echo {my_command} | clip')

    print(f"The command '{my_command}' has been copied to your clipboard.")

def send_payment(payment_method):

    if payment_method == "esewa":

        esewa_id = "9745477990"

        amount = input("Enter the amount you would like to send: ")

        print(f"Please send {amount} to eSewa ID {esewa_id}")

    elif payment_method == "paypal":

        paypal_email = "example@example.com"

        amount = input("Enter the amount you would like to send: ")

        print(f"Please send {amount} to {paypal_email} via PayPal.")

    elif payment_method == "bitcoin":

        bitcoin_address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"

        amount = input("Enter the amount you would like to send in BTC: ")

        print(f"Please send {amount} BTC to {bitcoin_address}")

    else:

        print("Invalid payment method")

if __name__ == "__main__":

    print("Welcome! Please select an option:")

    print("1. Open Facebook")

    print("2. Copy a Python command")

    print("3. Send payment")

    option = input()

    if option == "1":

        open_facebook()

    elif option == "2":

        copy_python_command()

    elif option == "3":

        payment_method = input("Enter the payment method (esewa/paypal/bitcoin): ")

        send_payment(payment_method)

    else:

        print("Invalid option")

