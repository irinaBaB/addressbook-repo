from models.group import Group


def test_case_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test1")))
    app.group.delete_first_group()
