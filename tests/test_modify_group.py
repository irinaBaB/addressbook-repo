from models.group import Group
from random import randrange


def test_case_modify_random_group(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test2")))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="bla1", header="bla2", footer="bla3")
    group.idg = old_groups[index].idg
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







