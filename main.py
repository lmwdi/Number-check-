import re
import urllib.request

# Get the mobile phone number from the user input
phone_number = input("Please enter your mobile phone number with the 98 prefix: ")




    # Construct the links to different applications for the phone number
    whatsapp_link = f"https://wa.me/{phone_number}"
    telegram_link = f"https://t.me/{phone_number}"

    # Check if the phone number is registered in WhatsApp by requesting the link
    try:
        response = urllib.request.urlopen(whatsapp_link)
        is_whatsapp_account = True
    except urllib.error.HTTPError:
        is_whatsapp_account = False

    # Check if the phone number is registered in Telegram by requesting the link
    try:
        response = urllib.request.urlopen(telegram_link)
        is_telegram_account = True
    except urllib.error.HTTPError:
        is_telegram_account = False

    # Print the results
    print(f"WhatsApp link: {whatsapp_link} - Account{' exists' if is_whatsapp_account else ' does not exist'}")
    print(f"Telegram link: {telegram_link} - Account{' exists' if is_telegram_account else ' does not exist'}")
