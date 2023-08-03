from models.contact import Contact
from models.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
group_name = "special_group"
contact_to_create = Contact(firstname="cheburashka", lastname="gena", email="gena-cheburashka@family.com")


def test_case_adding_contact_to_group_on_create(app, db):
    contact = Contact(firstname="Special", lastname="Contact", nickname="contact_spec", address="2/3 Small street", homephone="7845784578-02", mobilephone="997-89-706",
                        email="spec_contact@gmail.com", byear="1982", bmonth="April", bday="1", group_name=group_name)
    if len(db.get_group_name(group_name)) == 0:
        app.group.create((Group(name=group_name)))
    old_contacts = db.get_contacts_in_group_list()
    app.contact.create(contact)
    new_contacts = db.get_contacts_in_group_list()
    assert len(old_contacts)+1 == len(new_contacts)


def test_case_adding_existing_contact_to_the_group(app,db):
    #do not consider phantome objects cases here
    if len(db.get_group_name(group_name)) == 0:
        app.group.create(Group(name=group_name))
    random_group = (random.choice(db.get_group_list()))
    if len(orm.get_contacts_not_in_group(Group(id=random_group.id))) == 0:
        app.contact.create(contact_to_create)
    contact = random.choice(orm.get_contacts_not_in_group(Group(id=random_group.id)))

    old_contacts_in_groups = orm.get_contacts_in_group(Group(id=random_group.id))
    app.contact.add_contact_to_group(random_group.name, contact.id)
    new_contacts_in_groups = orm.get_contacts_in_group(Group(id=random_group.id))
    # this is a case when no contacts and groups exist
    if len(orm.get_contacts_in_group(Group(id=random_group.id))) == 0:
        assert len(old_contacts_in_groups) == len(new_contacts_in_groups)
        old_contacts_in_groups == new_contacts_in_groups
    # case of some contacts and groups exist
    if len(orm.get_contacts_in_group(Group(id=random_group.id))) > 0:
        assert len(old_contacts_in_groups) + 1 == len(new_contacts_in_groups)
        old_contacts_in_groups.append(contact)
        assert sorted(old_contacts_in_groups, key=Contact.id_or_max) == sorted(new_contacts_in_groups, key=Contact.id_or_max)



def test_case_delete_contact_from_the_group(app,db):
    old_contacts = db.get_contacts_in_group_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(group_name, contact.id)
    new_contacts = db.get_contacts_in_group_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts



