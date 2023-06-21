from models.group import Group


def test_case_create_group(app):
    app.group.create(Group(name="test1", header="one test", footer="second field"))


def test_case_create_group_empty_fields(app):
    app.group.create(Group(name="", header="", footer=""))
