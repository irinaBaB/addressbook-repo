from models.contact import Contact
from random import randrange
import random


def test_case_modify_contact(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_field = Contact(firstname="Nadia", lastname="Mahmud")
    app.contact.modify_contact_by_id(contact.id, contact_field)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id = contact_field
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)


# the tests below only modify the fist index
def test_case_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first(Contact(mobilephone='+745512385'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_case_modify_contact_date_of_birth(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first(Contact(bmonth='February', bday='15', byear='1954'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)