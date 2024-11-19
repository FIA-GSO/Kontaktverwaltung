#
# f.folkmann@gso.schule.koeln, 2022
#
"""contact manager functions"""
from contact import Contact
from models import Session, ContactModel
import uuid


def create_uuid():
    """create a universal unique identifier"""
    return str(uuid.uuid4())


def get_contact(uuid):
    """get contact by uuid"""
    session = Session()
    contact_model = session.query(ContactModel).filter_by(uuid=uuid).first()
    session.close()

    if contact_model is None:
        return None

    return Contact(contact_model.firstname, contact_model.lastname)


def get_contacts(patt=""):
    """get contacts optionally filtered by patt"""
    session = Session()
    query = session.query(ContactModel)

    if patt:
        query = query.filter(
            (ContactModel.firstname.like(f'%{patt}%')) |
            (ContactModel.lastname.like(f'%{patt}%'))
        )

    contacts = {}
    for contact_model in query.all():
        contact = Contact(contact_model.firstname, contact_model.lastname)
        contacts[contact_model.uuid] = contact

    session.close()
    return contacts


def save_contact(uuid, contact):
    """save contact to database"""
    session = Session()
    contact_model = ContactModel(
        uuid=uuid,
        firstname=contact.firstname,
        lastname=contact.lastname
    )

    existing = session.query(ContactModel).filter_by(uuid=uuid).first()
    if existing:
        existing.firstname = contact.firstname
        existing.lastname = contact.lastname
    else:
        session.add(contact_model)

    session.commit()
    session.close()


def delete_contact(uuid):
    """delete contact under given uuid"""
    session = Session()
    contact = session.query(ContactModel).filter_by(uuid=uuid).first()
    if contact:
        session.delete(contact)
        session.commit()
        session.close()
        return True
    session.close()
    return False


def add_contact(contact):
    """add contact under new individual uuid"""
    uuid = create_uuid()
    save_contact(uuid, contact)
    return uuid


if __name__ == "__main__":
    # Test code here
    contact1 = Contact("Hans", "Glück")
    contact2 = Contact("Erna", "Effel")
    id1 = add_contact(contact1)
    id2 = add_contact(contact2)
    print(get_contact(id1))
    print(get_contact(id2))
    delete_contact(id1)
    contacts = get_contacts()
    for uuid in contacts:
        print(uuid, contacts[uuid])
