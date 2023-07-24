from models.group import Group
import random
from random import randrange


def test_case_modify_random_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create((Group(name="test2")))
    old_groups = db.get_group_list()
    randome_group = random.choice(old_groups)
    group = Group(name="bla1", header="bla2", footer="bla3")
    app.group.modify_group_by_id(randome_group.id, group)
    new_groups =db.get_group_list()
    assert len(old_groups) == len(new_groups)
    randome_group.id = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







