# birthday_anniv
Birthday and Anniversary Auto Messages to Friends

The code is a Python program for sending birthday and anniversary reminders to a list of friends. It imports the necessary modules such as datetime, smtplib, os, random, csv, and email.

The list of friends and their details are defined in the dictionary friendsList. The program then defines a class called BirthdayReminder that has methods for sending emails and SMS, getting the current date, and sending reminders.

In the sendEmail method, it uses the smtplib module to send an email with a subject and message to the specified email address using the Google SMTP server. The sendSMS method is not implemented in the code but is defined as a placeholder for future development.

The get_today_date method returns the current date using the datetime module. The send_reminder method checks if today is the birthday or anniversary of each friend in the friendsList and sends a message to the appropriate email and SMS (if implemented) using the sendEmail and sendSMS methods respectively.

Finally, the program defines the main block to instantiate the BirthdayReminder class and call the send_reminder method.
