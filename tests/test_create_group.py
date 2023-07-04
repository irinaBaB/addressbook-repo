from models.group import Group



def test_case_create_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test1", header="one test", footer="second field")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() #hash
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_case_create_group_empty_fields(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="test1", header="one test", footer="second field")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups)+1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
