from models.group import Group


def test_case_adding_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test1", header="one test", footer="second field"))
    app.session.logout()


def test_case_adding_group_empty_fields(app):

    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
