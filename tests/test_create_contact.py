from fixture.application import Application
from models.contact import Contact
import pytest



@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_case_adding_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Petr", middlename="sergeevich", lastname="Ivanov", nickname="petya", address="2/3 Small street", homephone="089-56-67", mobilephone="997-89-706",
                        email="petay@gmail.com", byear="1982", bmonth="April", bday="1"))
    app.session.logout()

