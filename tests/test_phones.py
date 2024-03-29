import re
from models.contact import Contact

def test_phones_and_contacts_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert emails_cleaning(contact_from_home_page.email) == merge_emails_to_verify_with_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#ex:21
def test_contacts_from_db_check(app, db):
    contact_from_home_page_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_home_page_db) == len(contact_from_home_page)
    for index in range(len(contact_from_home_page)):
        assert contact_from_home_page[index].firstname == contact_from_home_page_db[index].firstname
        assert contact_from_home_page[index].lastname == contact_from_home_page_db[index].lastname
        assert contact_from_home_page[index].address == contact_from_home_page_db[index].address
        assert emails_cleaning(contact_from_home_page[index].email) == \
               merge_emails_to_verify_with_home_page(contact_from_home_page_db[index])
        assert contact_from_home_page[index].all_phones_from_home_page == \
               merge_phones_like_on_home_page(contact_from_home_page_db[index])

#WIP
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page_edited(0)
#     contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    #assert contact_from_view_page.homephone == contact_from_edit_page.homephone

    # assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    # assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    # assert contact_from_view_page.address == contact_from_edit_page.address

    #assert contact_from_view_page == merge_all_contacts_compare_with_view_page(contact_from_edit_page)


def clear(p):
    return re.sub("[() -]", "", p)


def clear_email_spaces(p):
    return re.sub(" ", "", p)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [
                                                                contact.homephone,
                                                                contact.mobilephone,
                                                                contact.workphone,
                                                                contact.secondaryphone]))))


def merge_emails_to_verify_with_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email_spaces(x),
                                filter(lambda x: x is not None, [
                                    contact.email,
                                    contact.email2,
                                    contact.email3]))))


def emails_cleaning(email):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email_spaces(x),
                                filter(lambda x: x is not None, [email]))))




