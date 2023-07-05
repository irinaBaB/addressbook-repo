import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    contact_from_view_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(p):
    return re.sub("[() -]", "", p)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone,
                                                                contact.mobilephone,
                                                                contact.secondaryphone,
                                                                contact.workphone]))))

def merge_all_contacts_view_page():
    pass
