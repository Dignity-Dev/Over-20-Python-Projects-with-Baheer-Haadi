# Building Email sending app

from email.message import EmailMessage
import ssl
import smtplib


email_sender = "SENDER EMAIL" #sender email e.g basheerhaadi3@gmail.com
email_password ='YOUR APP PASSWORD' # Gmail or any app password use is required


email_reciever = 'reciever email' # it can be signle or list ['kimlefirke@gufum.com','seped74315@vaband.com']

subject = "Learn by building 20 Project in python" #Suject of the Message

body = """
Do you wanna learn python programming? Here is a big opputunity for you to learn about python programming and how to use it in your application to build your project...
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
    
    
 