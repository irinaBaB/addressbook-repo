from models.contact import Contact


def test_case_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    old_contacts = app.contact.get_contact_list()
    contact_field = Contact(firstname="Nadia", lastname="Mahmud")
    contact_field.idc = old_contacts[0].idc
    app.contact.modify_first(contact_field)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact_field
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_case_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create((Contact(firstname="cheburashka")))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first(Contact(mobilephone='+745512385'))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)


def test_case_modify_contact_date_of_birth(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    old_groups = app.group.get_group_list()
    app.contact.modify_first(Contact(bmonth='February', bday='15', byear='1954'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)