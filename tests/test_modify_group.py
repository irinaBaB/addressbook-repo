from models.group import Group


def test_case_modify_group_empty_fields(app):

    app.session.login(username="admin", password="secret")
    app.group.modify_first_record(Group(name="bla1", header="bla2", footer="bla3"))
    app.session.logout()


def test_case_modify_group_name(app):

    app.session.login(username="admin", password="secret")
    app.group.modify_first_record(Group(name="only name"))
    app.session.logout()


def test_case_modify_group_header(app):

    app.session.login(username="admin", password="secret")
    app.group.modify_first_record(Group(header="new header"))
    app.session.logout()




