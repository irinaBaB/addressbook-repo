from models.contact import Contact


def test_case_create_contact(app):
    app.contact.create(Contact(firstname="Petr", middlename="sergeevich", lastname="Ivanov", nickname="petya", address="2/3 Small street", homephone="089-56-67", mobilephone="997-89-706",
                               email="petay@gmail.com", byear="1982", bmonth="April", bday="1"))

