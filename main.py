from contact import *




# Get all the contacts

CONTACTS_FILE = "contacts.txt"
contacts = []


#fills the contacts with the contacts from the file
def getAllContacts(contacts:list, contactFile=CONTACTS_FILE):

    with open(contactFile, "r") as file:
        while(True):
            line = file.readline()
            if(line == ""):
                return
            print(line)
            contact = parseContact(line)
            contacts.append(contact)
        
    


#Saves all the contacts to the file.
def saveContacts(contacts, contactFile=CONTACTS_FILE):
    
    with open(contactFile, "w") as file:
        for contact in contacts:
            file.write(str(contact))
        

def printAllContacts(contacts):
    for i in range(1, len(contacts) + 1):
        
        print(f"{i} : {contacts[i - 1]}")


getAllContacts(contacts, CONTACTS_FILE)
printAllContacts(contacts)
saveContacts(contacts)















