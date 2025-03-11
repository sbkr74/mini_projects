from email.message import EmailMessage
import ssl
import smtplib
sender_email = "sbkr74@gmail.com"
sender_password = ""

reciever_mail = ""
subject = "[IMP]* Message generated through system! ..."
body = """
This message is generated through python code. 
                                    regards,
                                    Devil
"""

em = EmailMessage()
em['From'] = sender_email
em['To'] = reciever_mail
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender_email,sender_password)
    smtp.send_message(sender_email,reciever_mail,em.as_string())