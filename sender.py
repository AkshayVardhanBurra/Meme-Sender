from main import getAllContacts
from contact import *
from concurrent.futures import ThreadPoolExecutor
import time
import requests
import random
from twilio.rest import Client
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "burraakshay5@gmail.com"
password = "bckn hxtc frpn lrjh"

context = ssl.create_default_context()


INTERVAL = 0.5

HUMOR_API_KEY = "26ad20b26a024bb0b0d45fdbce9d03d4"

giphy_api_key = "TLTMWF0FhXitJrVmFJV5J3rDR2guU0ES"

ACCOUNT_SID = "AC3057811b7ba3ebdf93c2a82e2bb07fef"

AUTH_TOKEN = "1b3e62442618a903503c1c2b88a7e6e9"

MAX_LENGTH = 70


categories = ["dogs", "cats", "motivation", "food", "music"]

contacts = []
getAllContacts(contacts)
client = Client(ACCOUNT_SID, AUTH_TOKEN)

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
except:
     print("[-] Cannot connect to email system!")
     sys.exit()






#sends the meme to a contact. this task will go in the threadpool
def sendSMS(contact:Contact, meme, type):

    
    random_part = None

    if type == "jokes":
        random_part = "Joke of the day: " + meme["jokes"][random.randint(0, len(meme["jokes"]) - 1)]["joke"]
    else:
        random_part = "Meme of the day: " + meme["data"][random.randint(0, len(meme["data"]) - 1)]["images"]["original"]

    print(f"in here sending to: {contact.phoneNumber}. the message is: {random_part}")
    
    message = client.messages.create(
    from_='+18886914243',
    body=random_part,
    to=f"{contact.countryCode}{contact.phoneNumber}"
    )

    print("has been sent?")



def send_email(img_meme, contact:Contact):
     
     random_meme = img_meme["data"][random.randint(0, len(img_meme["data"]) - 1)]
     print("trying to send: ")
     print("URL: " + str(random_meme))
     email_body = construct_email_message(random_meme, contact)
     print(email_body.as_string())

     server.sendmail(sender_email, contact.mail, email_body.as_string())
    

#returns an EmailMessage
def construct_email_message(meme, contact:Contact):
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Messed Up Meme: {meme["title"]}"
    message["From"] = sender_email
    message["To"] = contact.mail

    htmlMessage = f"""
        <html>
        <body>
            <img src="{meme["images"]["original"]["url"]}"/>
            <h3>
            {meme["title"]}
            </h3>
            </body>
        </html>

    """

    regularMessage = f"""
        img: {meme["images"]["original"]}
        desc: {meme["title"]}
    """

    part1 = MIMEText(htmlMessage, "html")
    part2 = MIMEText(regularMessage, "plain")

    message.attach(part2)
    message.attach(part1)
    


    return message
    




def send_meme(meme_img, meme_text, contact:Contact):
     print("sending meme to: " + contact.name + " sms status: " + str(contact.hasSMS))

    # uncomment when twilio is back up
    #  if(contact.hasSMS):
    #       print("in here")
    #       sendSMS(contact, meme_text, "jokes")
    #       #sendSMS(contact, meme_img, "gif")
     
     if(contact.mail.strip() != ""):
        try:
            send_email(meme_img, contact)
        except Exception as e:
             print("[-] couldn't send email!")
             print(e)

     #Send the meme email

    
     
     


def generateRandomCategoryURL(categories, type="gif"):
    category = categories[random.randint(0, len(categories) - 1)]
    if type == "jokes":
         return f"https://api.humorapi.com/jokes/search?number=30&keywords={category}&api-key={HUMOR_API_KEY}&max-length={MAX_LENGTH}"
    else:
        return f"https://api.giphy.com/v1/gifs/search?api_key={giphy_api_key}&q={category}&limit=60&offset=0&rating=g&lang=en&bundle=messaging_non_clips"

def get_meme(type="memes"):
        meme_request = requests.get(url=generateRandomCategoryURL(categories, type))
        if(meme_request.status_code == 200):
            
            return meme_request.json()
        else:
            
            raise ValueError()
        


# with ThreadPoolExecutor(max_workers=4) as pool:

while(True):

        try:
        
            meme_img = get_meme("memes")
#             meme_img={
#     "memes": [
#         {
#             "id": 6696,
#             "url": "https://i.imgur.com/1rmAxUG.jpg",
#             "type": "image/jpeg",
#             "description":"yes"
#         },
#         {
#             "id": 6697,
#             "url": "https://i.imgur.com/ELT8zMQ.jpg",
#             "type": "image/jpeg",
#             "description":"yes"
#         },
#         {
#             "id": 6698,
#             "url": "https://i.imgur.com/8JTc5z3.jpg",
#             "type": "image/jpeg",
#             "description":"yes"
#         }
#     ],
#     "available": 32
# }
            # meme_text = get_meme("jokes")
            meme_text = "examplejoke"

            for contact in contacts:
                
                send_meme(meme_img, meme_text, contact)


            time.sleep(INTERVAL * 60)
        except ValueError:
            print("Damn the api key ran out!")
            break

        
print("ending program lil bro")







        
    
        






#outputs a url that gets categories from

