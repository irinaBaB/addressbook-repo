from models.group import Group


def test_case_create_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test1", header="one test", footer="second field"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)

def test_case_create_group_empty_fields(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
