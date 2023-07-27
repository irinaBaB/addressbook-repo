from models.contact import Contact
from models.group import Group
import random


group_name = "special_group"

def test_case_adding_contact_to_group(app, db):
    contact = Contact(firstname="Special", lastname="Contact", nickname="contact_spec", address="2/3 Small street", homephone="7845784578-02", mobilephone="997-89-706",
                        email="spec_contact@gmail.com", byear="1982", bmonth="April", bday="1", group_name=group_name)
    if len(db.get_group_name(group_name)) == 0:
        app.group.create((Group(name=group_name)))
    old_contacts = db.get_contacts_in_group_list()
    app.contact.create(contact)
    new_contacts = db.get_contacts_in_group_list()
    assert len(old_contacts)+1 == len(new_contacts)


def test_case_delete_contact_from_the_group(app,db):
    old_contacts = db.get_contacts_in_group_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(group_name, contact.id)
    new_contacts = db.get_contacts_in_group_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts



