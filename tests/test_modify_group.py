from models.group import Group


def test_case_modify_group_empty_fields(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test2")))
    old_groups = app.group.get_group_list()
    group = Group(name="bla1", header="bla2", footer="bla3")
    group.idg = old_groups[0].idg
    app.group.modify_first_record(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_case_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create((Group(name="test2")))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_record(Group(name="only name"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_case_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create((Group(name="test2")))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_record(Group(header="new header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)





