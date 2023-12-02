import yagmail
import os

#This code no longer works due to gmail's updated policy on third-party prohibition

sender = os.environ.get('SMTP_USER')
password = os.environ.get('SMTP_PASSWORD')
receiver = os.environ.get('SMTP_RECEIVER')

print (f"sender : {sender} \npassword : {password} \nreceiver : {receiver}")

subject = """
This is the subject!
"""
contents = """
Here is the content of the email.
Please open this.
"""

yag = yagmail.SMTP(sender, password)
yag.send(to=receiver, subject=subject, contents=contents)

print("Email has been sent!")