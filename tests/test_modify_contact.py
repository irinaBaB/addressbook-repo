from models.contact import Contact


def test_case_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    app.contact.modify_first(Contact(firstname="Nadia", lastname="Mahmud", email="nadia@gmail.com"))


def test_case_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    app.contact.modify_first(Contact(mobilephone='+745512385'))


def test_case_modify_contact_date_of_birth(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="cheburashka")))
    app.contact.modify_first(Contact(bmonth='February', bday='15', byear='1954'))