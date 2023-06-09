import urllib.parse
import requests

# Get the mobile phone number from the user input
phone_number = input("Please enter your mobile phone number: ")

# Construct the links to different applications for the phone number
whatsapp_link = f"https://wa.me/{phone_number}"
telegram_link = f"https://t.me/{phone_number}"

# Check if the phone number is registered in WhatsApp by sending a GET request to the link
whatsapp_response = requests.get(whatsapp_link)
is_whatsapp_account = whatsapp_response.status_code == 200

# Check if the phone number is registered in Telegram by sending a GET request to the link
telegram_response = requests.get(telegram_link)
is_telegram_account = telegram_response.status_code == 200

# Print the results
print(f"WhatsApp link: {whatsapp_link} - Account{' exists' if is_whatsapp_account else ' does not exist'}")
print(f"Telegram link: {telegram_link} - Account{' exists' if is_telegram_account else ' does not exist'}")
