from models.contact import Contact


def test_case_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

