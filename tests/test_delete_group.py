import random

from models.group import Group
from random import randrange


def test_case_delete_any_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create((Group(name="test1")))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups.remove(group)
    #old_groups[index:index+1] = []
    assert old_groups == new_groups

