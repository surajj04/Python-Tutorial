contactList = []


def addContact(contact):
    contact.cid = len(contactList) + 1
    contactList.append(contact)


def getContactList():
    return contactList


def updateContactList(contact):
    c = contactList.index(contact.cid - 1)
    contact.name = c.name
    contact.phoneNo = c.phoneNo
    contact.email = c.email
    contact.address = c.address


def deleteContact(id):
    contact = contactList.index(id - 1)
    contactList.remove(contact)
