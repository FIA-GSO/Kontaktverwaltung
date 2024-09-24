#
# f.folkmann@gso.schule.koeln, 2022
#
"""client calling remote 'contacts_api'"""
from requests import post, get, delete, put
from json import dumps, loads
from contact import Contact

import logging
logging.basicConfig(level = logging.ERROR)

api_url_base = "http://127.0.0.1:5000"

def get_contact(uuid):
    """get contact by uuid"""
    api_url = f"{api_url_base}/get_contact/{uuid}"
    logging.debug(f"C: GET get_contact: {uuid}")
    resp = get(api_url, params = uuid)
    dict = loads(resp.text)
    contact = Contact.from_dict(dict)
    logging.debug(f"C: Resp: {resp.status_code}, contact '{str(contact)}'")
    return contact

def get_contacts(patt = ""):
    """get contacts optionally filtered by patt"""
    api_url = f"{api_url_base}/get_contacts"
    if patt != "": api_url += f"/{patt}"
    logging.debug(f"C: GET get_contacts: {patt}")
    resp = get(api_url, params = patt)
    dict = loads(resp.text)
    # reconvert transmitted dictionaries to contacts
    for uuid in dict.keys():
        contact = Contact.from_dict(dict[uuid])
        dict[uuid] = contact
    logging.debug(f"C: Resp: {resp.status_code}, {len(dict)} contacts")
    return dict

def add_contact(contact):
    """add contact under new individual uuid"""    
    api_url = f"{api_url_base}/add_contact"
    dict = contact.to_dict()
    json = dumps(dict)
    logging.debug(f"C: POST add_contact: {json}")
    resp = post(api_url, json = json)
    uuid = resp.text
    logging.debug(f"C: Resp: {resp.status_code}, uuid '{uuid}'")
    return uuid

def save_contact(uuid, contact):
    """saves contact under given uuid"""
    raise NotImplementedError
    return uuid

def delete_contact(uuid):
    """delete contact under given uuid"""
    api_url = f"{api_url_base}/delete_contact/{uuid}"
    logging.debug(f"C: DELETE delete_contact: {uuid}")
    resp = delete(api_url, params = uuid)
    logging.debug(f"C: Resp: {resp.status_code}, {resp.text}")
    return resp.status_code == 200

if __name__ == "__main__":
    #test code here
    uuid1 = add_contact(Contact("theo","test"))
    uuid2 = add_contact(Contact("elli","eilig"))

