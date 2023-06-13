import pytest
from models.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_case_adding_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="test1", header="one test", footer="second field"))
    app.session.logout()


def test_case_adding_group_empty_fields(app):

    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
