from models.contact import Contact


def test_case_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Petr", middlename="sergeevich", lastname="Ivanov", nickname="petya", address="2/3 Small street", homephone="089-56-67", mobilephone="997-89-706",
                               email="petay@gmail.com", byear="1982", bmonth="April", bday="1")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

