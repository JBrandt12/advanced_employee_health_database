import requests
from bs4 import BeautifulSoup
import smtplib
import email.message



def send_email(msg): 
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        ID = 'python.flutter01@gmail.com'
        PASSWORD = 'Dogfoodlid1!'
        email_reciever = 'brandt.jon@gmail.com'
        # email_reciever = '2403709723@pm.sprint.com '
        server.login(ID, PASSWORD)
        message =  "{}"
        # message =  '{}'
        server.sendmail(ID, email_reciever, message)

        print('Success')
    except Exception as e:
            print(e)
    finally: 
            server.quit()


msg = email.message.Message()


# subject = "Report"

send_email(msg)