from utils.Cli import *
from service.ContactService import *
import os


def clear_screen():
    os.system('clear')


def choice(x):
    if x == 1:
        clear_screen()
        contact = add_contact()
        addContact(contact)
    elif x == 2:
        clear_screen()
        cid = delete_contact()
        deleteContact(cid)
    elif x == 3:
        clear_screen()
        contact = update_contact(getContactList())
        updateContactList(contact)
    elif x == 4:
        clear_screen()
        get_contact_details(getContactList())
    elif x == 5:
        clear_screen()
        show_all_contacts(getContactList())
