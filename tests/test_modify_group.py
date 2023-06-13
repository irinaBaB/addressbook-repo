from models.group import Group


def test_case_create_group_empty_fields(app):

    app.session.login(username="admin", password="secret")
    app.group.modify_first_record(Group(name="bla1", header="bla2", footer="bla3"))
    app.session.logout()
