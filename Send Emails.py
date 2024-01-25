#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os 
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'Email@gmail.com'
email_password = 'Password'  # Ensure this environment variable is correctly set
email_receiver = 'Email@gmail.com'

subject = 'Hey, this is sent from Python'
body = 'Yo'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()  

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
print("Email sent successfully!")


# In[ ]:




