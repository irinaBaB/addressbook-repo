from models.group import Group


def test_case_modify_group_empty_fields(app):

    app.group.modify_first_record(Group(name="bla1", header="bla2", footer="bla3"))


def test_case_modify_group_name(app):
    app.group.modify_first_record(Group(name="only name"))


def test_case_modify_group_header(app):
    app.group.modify_first_record(Group(header="new header"))





