
DELIMETER = "|"

class Contact:
    
    def __init__(self, name, phoneNumber, hasWhatsApp, hasSMS, mail, totalMessages, countryCode="+1"):
        self.name = name
        self.phoneNumber = phoneNumber
        self.hasWhatsApp = hasWhatsApp
        self.totalMessages = totalMessages
        self.hasSMS = hasSMS
        self.countryCode=countryCode
        self.mail = mail
    
    def __str__(self):
        return self.name + DELIMETER + str(self.phoneNumber) + DELIMETER + str(self.hasWhatsApp) + DELIMETER + str(self.hasSMS) +  DELIMETER + str(self.mail) + DELIMETER + str(self.totalMessages)+ DELIMETER+ str(self.countryCode) 
    


def isValidPhoneNumber(number):
    return len(number) == 10


#takes in the string version of contact and parses it into a Contact
def parseContact(contactStr:str):
    splitted = contactStr.split(DELIMETER)
    print(splitted)
    return Contact(splitted[0], int(splitted[1]), bool(splitted[2]), bool(splitted[3]), splitted[4], splitted[5], splitted[6])


