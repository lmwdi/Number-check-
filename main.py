import urllib.parse
import requests
from prettytable import PrettyTable
import os

# Get the mobile phone number from the user input
phone_number = input("Please enter your mobile phone number [without '0']: ")

# Construct the links to different applications for the phone number
whatsapp_link = f"https://wa.me/+98{phone_number}"
telegram_link = f"https://t.me/+98{phone_number}"

print('Please Wait...')

try:
    # Create a table to display the results
    table = PrettyTable()
    table.field_names = ["Application", "Link", "Registered"]

    # Check if the phone number is registered in WhatsApp by sending a GET request to the link
    whatsapp_response = requests.get(whatsapp_link)
    is_whatsapp_account = whatsapp_response.status_code == 200
        
    # Add the WhatsApp result to the table
    table.add_row(["WhatsApp", whatsapp_link, "✓" if is_whatsapp_account else "✕"])

    # Check if the phone number is registered in Telegram by sending a GET request to the link
    telegram_response = requests.get(telegram_link)
    is_telegram_account = telegram_response.status_code == 200

    # Add the Telegram result to the table
    table.add_row(["Telegram", telegram_link, "✓" if is_telegram_account else "✕"])
except:
    print('error')

# Print the table
os.system('clear')
print(table)
