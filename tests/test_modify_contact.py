from models.contact import Contact


def test_case_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(firstname="Nadia", lastname="Mahmud", email="nadia@gmail.com"))
    app.session.logout()


def test_case_modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(mobilephone='+745512385'))
    app.session.logout()


def test_case_modify_contact_date_of_birth(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(bmonth='February', bday='15', byear='1954'))
    app.session.logout()
