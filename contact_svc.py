#
# f.folkmann@gso.schule.koeln, 2022
#
"""contact manager functions"""
from contact import Contact
import os
import uuid

def data_dir():
    """contacts data directory"""
    return "data"

# create data directory if not exist
os.makedirs(data_dir(), exist_ok=True)

def create_uuid():
    """create a universal unique identifier"""
    return str(uuid.uuid4())

def contact_file_name(uuid):
    """get contact filename by uuid"""
    return f"{data_dir()}/{uuid}.csv"

def get_contact(uuid):
    """get contact by uuid"""
    print('SVC TO DO: get_contact()')
    return Contact('Max', 'Muster')

def get_contacts(patt = ""):
    """get contacts optionally filtered by patt"""
    contacts = {}
    print('SVC TO DO: get_contacts()')
    contacts[str(uuid.uuid4())] = Contact('Mia', 'Muster')
    contacts[str(uuid.uuid4())] = Contact('Kia', 'Klabuster')
    return contacts


def add_contact(contact):
    """add contact under new individual uuid"""    
    uuid = create_uuid()
    print('SVC TO DO: add_contact()')
    return uuid

def save_contact(uuid, contact):
    """saves contact under given uuid"""
    print('SVC TO DO: save_contact()')
    pass

def delete_contact(uuid):
    """delete contact under given uuid"""
    print('SVC TO DO: delete_contact()')
    return True

if __name__ == "__main__":
    #test code here
    if True:
        save_contact(create_uuid(), Contact("Hans", "Glück"))
        save_contact(create_uuid(), Contact("Erna", "Effel"))
        id = add_contact(Contact("Zorro", "Held"))
        print(get_contact(id))
        delete_contact(id)
        contacts = get_contacts()
        for uuid in contacts:
            print(uuid, contacts[uuid])
