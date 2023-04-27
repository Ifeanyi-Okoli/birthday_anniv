"""
The code is a Python program for sending birthday and anniversary reminders to a list of friends. It imports the necessary modules such as datetime, smtplib, os, random, csv, and email.

The list of friends and their details are defined in the dictionary friendsList. The program then defines a class called BirthdayReminder that has methods for sending emails and SMS, getting the current date, and sending reminders.

In the sendEmail method, it uses the smtplib module to send an email with a subject and message to the specified email address using the Google SMTP server. The sendSMS method is not implemented in the code but is defined as a placeholder for future development.

The get_today_date method returns the current date using the datetime module. The send_reminder method checks if today is the birthday or anniversary of each friend in the friendsList and sends a message to the appropriate email and SMS (if implemented) using the sendEmail and sendSMS methods respectively.

Finally, the program defines the main block to instantiate the BirthdayReminder class and call the send_reminder method.
"""


#======IMPORTING OF RELEVANT MODULES======
import datetime  # importing datetime module
import smtplib  # importing smtplib module for email
import os
import random
import csv
import email
import ssl  # importing ssl module for email
# from decouple import config  # importing config file for email



# ====================DICTIONARY OF LIST OF FRIENDS AND THEIR DETAILS====================
friendsList = {
    "Jacob": {"birthday": "25-04-1980", "anniversary": "30-04-2010", "phone": "1234567890", "email": "fnykly@gmail.com"},
    "Richard": {"birthday": "26-04-1980", "anniversary": "29-04-2010", "phone": "+2348035138223", "email": "ituaakhideno@gmail.com"},
    "Simon": {"birthday": "27-04-1980", "anniversary": "28-04-2010", "phone": "+234178593456", "email": "fnykly@gmail.com"},
    "Peter": {"birthday": "01-05-1980", "anniversary": "02-05-2010", "phone": "1234567890", "email": "fnykly@gmail.com"},
}


# ====================CLASS DEFINITION====================
class BirthdayReminder:
# =======================METHOD FOR INITIALIZATION======================
    def __init__(self, friendsList):
        self.friendsList = friendsList
        self.smtpServer = "smtp.gmail.com"
        self.smtpPort = 465
        self.context = ssl.create_default_context()
        # self.myEmail = config("EMAIL_ADDRESS")
        # self.myPassword = config("PASSWORD")
        self.myEmail = "ituaakhideno@gmail.com"
        self.myPassword = "avjuidsxksgzhnum"

# =======================METHOD FOR SENDING EMAIL======================
    def sendEmail(self, subject, message, to_email):
        with smtplib.SMTP_SSL(self.smtpServer, port=self.smtpPort, context=self.context) as server:
            server.login(self.myEmail, self.myPassword)
            server.sendmail(self.myEmail, to_email, f"Subject: {subject}\n\n{message}")


# =======================METHOD FOR SENDING SMS======================
    def sendSMS(self, phone_num, message):
        # code to send SMS
        pass

# ========================METHOD FOR GETTING TODAY'S DATE=======================
    def get_today_date(self):
        today = datetime.date.today()
        return today


# ========================METHOD FOR SENDING REMINDER BY CALLING THE SENDEMAIL AND SENDSMS METHODS===========================
    def send_reminder(self):
        today = self.get_today_date()
        for friend, details in self.friendsList.items():
            # Check if today is friend's birthday
            bday = datetime.datetime.strptime(details["birthday"], '%d-%m-%Y').date()
            if today.month == bday.month and today.day == bday.day:
                # Send birthday email
                subject = f"Happy Birthday {friend}!"
                message = f"Dear {friend},\n\nWishing you a very happy birthday! Have a wonderful day.\n\nBest Regards,\nIfeanyi Okoli"
                to_email = details["email"]
                phone_num = details["phone"]
                self.sendEmail(subject, message, to_email)
                self.sendSMS(phone_num, message)
                print("successful")

            # Check if today is friend's anniversary
            anniv = datetime.datetime.strptime(details["anniversary"], '%d-%m-%Y').date()
            if today.month == anniv.month and today.day == anniv.day:
                # Send anniversary email
                subject = f"Happy Anniversary {friend}!"
                message = f"Dear {friend},\n\nWishing you a very happy wedding anniversary! May your love continue to grow stronger with each passing year.\n\nBest Regards,\nIfeanyi Okoli"
                to_email = details["email"]
                self.sendEmail(subject, message, to_email)

# ========================MAIN BLOCK===============================================
if __name__ == '__main__':  #This is the entry point of the program
    birthday_reminder = BirthdayReminder(friendsList)  #Create an instance of the BirthdayReminder class
    birthday_reminder.send_reminder() #Call the send_reminder method of the BirthdayReminder class using the dot notation
