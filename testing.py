




# from twilio.rest import Client
# account_sid = 'AC3057811b7ba3ebdf93c2a82e2bb07fef'
# auth_token = "1b3e62442618a903503c1c2b88a7e6e9"
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   from_='+18886914243',
#   body='hello this is a test lil nigga',
#   to='+18777804236'
# )
# print(message.sid)



import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "burraakshay5@gmail.com"
password = "bckn hxtc frpn lrjh"

# Create a secure SSL context
context = ssl.create_default_context()


receiver_email = "dearakhi@gmail.com"
message1 = """\
<html>
  <body>
    <h1> this shit is in html </h1>
  <body>
</html>
"""

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

part1 = MIMEText(message1, "plain")
part2 = MIMEText(message1, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)

    
    
    # TODO: Send email here
    print("sending email: ")
    server.sendmail(sender_email, receiver_email, message.as_string())


except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 

print(server)

