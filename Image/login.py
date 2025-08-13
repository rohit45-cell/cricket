import pywhatkit
import datetime
import time
def login():
    cor_username="Ganesh"
    cor_password="Ganesh.45"
    username=input("enter the username:")
    password=input("Enter the password:")
    if cor_username==username and cor_password==password:
        print("The user login successfully")
        phone_number = "+917092459845"
        message = "Hello! Ganesh has logged in successfully."
        
    
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 2

        print("📤 Sending WhatsApp message in 2 minutes...")
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        
    else:
        print("invalid login")
login()