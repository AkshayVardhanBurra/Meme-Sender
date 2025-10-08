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
            file.write(str(contact).strip() + "\n")
        

def printAllContacts(contacts):
    for i in range(1, len(contacts) + 1):
        
        print(f"{i} : {contacts[i - 1]}")


getAllContacts(contacts)











#returns a number
def get_valid_choice():
    index = int(input("Enter the index: "))

    while index > len(contacts) or index < 1:
        index = int(input("Enter a proper index: "))
    
    return index - 1

def updateContact(contact:Contact):
    contact.name = input("Enter a name: ")
    contact.phoneNumber = int(input("Enter a phone number: "))
    contact.mail = input("Enter a mail: ")
    contact.countryCode = input("Enter a country code: ")
    contact.hasSMS = input("Has SMS? (y/n)") == "y"
    contact.hasWhatsApp = input("Has WhatsApp (y/n)") == "y"

def createContact():
    name = input("Enter a name: ")
    phoneNumber = int(input("Enter a phone number: "))
    mail = input("Enter a mail: ")
    countryCode = input("Enter a country code: ")
    hasSMS = input("Has SMS? (y/n)") == "y"
    hasWhatsApp = input("Has WhatsApp (y/n)") == "y"

    return Contact(name, phoneNumber, hasWhatsApp, hasSMS, mail, 0, countryCode)


user_choice = input("VIEW, UPDATE, DELETE, or CREATE: ")
while user_choice != "quit":

    if user_choice == "VIEW":
        printAllContacts(contacts)
    
    elif user_choice == "UPDATE" and len(contacts) > 0:
        printAllContacts(contacts)
        valid_index = get_valid_choice()
        updateContact(contacts[valid_index])
        saveContacts(contacts, CONTACTS_FILE)
    elif user_choice == "CREATE":
        new_contact = createContact()
        contacts.append(new_contact)
        saveContacts(contacts, CONTACTS_FILE)
        
    elif user_choice == "DELETE" and len(contacts) > 0:
        printAllContacts(contacts)
        valid_index = get_valid_choice()
        contacts.pop(valid_index)
        saveContacts(contacts, CONTACTS_FILE)
       
    else:
        print("Something must have been wrong with the input!")

    user_choice = input("VIEW, UPDATE, DELETE, or CREATE: ")










