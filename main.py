import csv
import requests
from email.message import EmailMessage
import smtplib

from email.mime.text import MIMEText

from Validation import*

SENDER = input("Please Enter your mail ID : ")
PASSWORD = input("Please Enter your mail password : ")

def send_email(subject):
    try:
        with open("sample.csv") as file:
            reader = csv.reader(file)
            next(reader)
                
            for Message , addr , Phone , Country , Schedule in reader:
                email_address = addr
                response = requests.get(
                    "https://isitarealemail.com/api/email/validate",
                    params = {'email': email_address})

                status = response.json()['status']           
                if status == "valid":
                    print("******************************************")
                    print(f"{addr} : email is valid")                   
                    msg = EmailMessage()
                    html = '''
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <style>
                            .container{
                                width: 300px;
                                border: 15px solid green;
                                padding: 50px;
                                margin: 20px;


                            }
                        </style>
                    </head>
                    <body>
                    <div class="container">
                        
                        <p style="color:blue">'''+Message+'''</p>
                        <a href="https://www.sms-magic.com/" target="_parent"><button>Visit Screen-Magic!</button></a>
                        
                    </div>
                    </body>
                    </html>
                    '''
                    Message = MIMEText(html , "html")

                    msg.set_content(Message)
                    msg["Subject"] = subject
                    msg["From"] = SENDER
                    msg["To"] = addr
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.login(SENDER, PASSWORD)                    
                    server.send_message(msg)
                    server.quit()
                    print(f'Sent to {addr}')
                elif status == "invalid":
                    print(f"{addr} : email is invalid")
                else:
                    print("email was unknown")
                checkValidefields(Phone)
                Check_message_content(Message)
                print(f"Country of candidate {Country}")
                print(f"Email will send on {Schedule}")
                print("************************************************************")
                                            
        print("Successful Sent Email")
        

            
    except:
        print("Email Sent Failed : Please check all requirement ")




send_email(subject="Screen-Magic")

