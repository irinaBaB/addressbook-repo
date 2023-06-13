from models.contact import Contact


def test_case_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Nadia", lastname="Mahmud", middlename='', nickname='', email="nadia@gmail.com",
                                             address="", homephone="", mobilephone="", byear="1990", bmonth="January", bday="10"))
    app.session.logout()
