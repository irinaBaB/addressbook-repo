from models.contact import Contact


def test_case_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    app.contact.delete_contact()

