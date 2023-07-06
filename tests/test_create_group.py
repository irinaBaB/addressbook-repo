import pytest

from models.group import Group
import random
import string


def randon_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=randon_string("name",8), header=randon_string("header", 7), footer=randon_string("footer",5))
    for i in range(3)]


@pytest.mark.parametrize('group', test_data, ids=[repr(x) for x in test_data])
def test_case_create_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() #hash
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
