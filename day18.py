#Writing a program using Functions modules
'''
SMTP module
email.message
vduz tgva carw lpez
'''

import smtplib
from email.message import EmailMessage

sender_email = "manojsai2710@gmail.com"
password = "jkfd ubsx vbss speu"
receiver_email = "mmsai3127@gmail.com"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = "Welcome Mail"
message.set_content(f"""
Hello Manoj!!



WELCOME TO OUR PYTHON CLASSES



Regards,
Pthon Team
""")

try :
    smtp = smtplib.SMTP("smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.send_message(message)
    print("Email sent successfully")
except Exception as e:
    print("Error: ",e)
finally:
    smtp.quit()
    




















