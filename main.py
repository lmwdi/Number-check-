import requests
from prettytable import PrettyTable

# Get the mobile phone number from the user input
phone_number = input("Please enter your mobile phone number: ")

# Construct the links to different applications for the phone number
whatsapp_link = f"https://wa.me/{phone_number}"
telegram_link = f"https://t.me/{phone_number}"

# Create a table to display the results
table = PrettyTable()
table.field_names = ["Application", "Link", "Registered"]

# Check if the phone number is registered in WhatsApp by sending a GET request to the link
whatsapp_response = requests.get(whatsapp_link)
if whatsapp_response.status_code == 200 and 'phone' in whatsapp_response.text:
    is_whatsapp_account = True
    table.add_row(["WhatsApp", whatsapp_link, "✓"])
else:
    is_whatsapp_account = False
    table.add_row(["WhatsApp", whatsapp_link, "✕"])

# Check if the phone number is registered in Telegram by sending a GET request to the link
telegram_response = requests.get(telegram_link)
if telegram_response.status_code == 200 and 'tgme_user_info_header_info' in telegram_response.text:
    is_telegram_account = True
    table.add_row(["Telegram", telegram_link, "✓"])
else:
    is_telegram_account = False
    table.add_row(["Telegram", telegram_link, "✕"])

# Print the table
print(table)
