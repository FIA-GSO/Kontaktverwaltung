#
# f.folkmann@gso.schule.koeln, 2022
#
"""contact app using local or remote 'contact_svc'"""
from contact import Contact

if True:
    # run over local service
    import contact_svc as mngr
else:
    # run over remove service via api-client
    import contact_client as mngr
    from requests.exceptions import RequestException

def show_contacts(contacts):
    """shows the loaded contacts"""
    for index in range(len(contacts)):
        show_contact(index+1, contacts[index])

def show_contact(num, contact):
    """shows a numbered contact"""
    print(f"Kontakt {num}")
    print(f" * Vorname : {contact.firstname}")
    print(f" * Nachname: {contact.lastname}")

def input_contact():
    """lets the user input a new contact"""
    print(f"\nGeben Sie neue Kontaktdaten ein (oder nichts für Ende)")
    firstname = input(" * Vorname  : ")
    if firstname == "": return None
    contact = Contact(
        firstname,
        input(" * Nachname : "),
    )
    return contact
    
def edit_contact(contact):
    """lets the user edit a contact"""
    print(f"\nÄndern Sie die Werte (oder nichts für Beibehalten)")
    edit_attribute(contact, "firstname", "Vorname")
    edit_attribute(contact, "lastname", "Nachname")

def edit_attribute(contact, attr_name, attr_display):
    value = input(f" * {attr_display:<8} : {getattr(contact, attr_name)} ? ")
    if value != "": setattr(contact, attr_name, value)

# ----- application functions

def show_menu():
    list = []
    while True:
        print("\nOptionen (#=Kontaktnummer, ?=Muster):")
        print(" a  Alle Kontakte anzeigen" )
        print(" f? Kontakt(e) finden" )
        print(" n  Neuen Kontakt zufügen " )
        print(" b# Kontakt bearbeiten " )
        print(" l# Kontakt löschen" )
        print(" x  Beenden" )
        command = input("> ")
        patt = ""
        try:
            opt = command[0:1]
            if opt == "f":
                patt = command[1:].strip()
                opt = "a"
                # fall through
            if opt == "a":
                list = []
                dict = mngr.get_contacts(patt)
                # combine uuid and contact in tupel list
                for uuid, contact in dict.items():
                    list.append((uuid, contact))
                # sort list by firstname
                list = sorted(list, key=lambda x: getattr(x[1], "firstname"))
                # display items
                for i in range(len(list)):
                    show_contact(i+1, list[i][1])
                continue
            if opt == "n":
                contact = input_contact()
                mngr.add_contact(contact)
                continue
            if opt == "b":
                num = int(command[1:])-1
                uuid = list[num][0]
                contact = list[num][1]
                edit_contact(contact)
                mngr.save_contact(uuid, contact)
                continue
            if opt == "l":
                num = int(command[1:])-1
                uuid = list[num][0]
                mngr.delete_contact(uuid)
                continue
            if opt == "x":
                break
        except RequestException as exc1:
            print("\nServer nicht ansprechbar!")
            print(type(exc1))
        except Exception as exc2:
            print("\nUngültige Eingabe!")
            print(type(exc2))

import sys # regarding sys.argv    

def main():
    """application main program"""
    print("\n***** My Contacts *****")
    show_menu()
    print("Bye.")

if __name__ == "__main__":
	main()
#
# End of code
#
