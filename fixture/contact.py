from selenium.webdriver.support.ui import Select
from models.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.app.open_home_page()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_create_contact_page()
        wd.find_element_by_name("theform").click()
        self.filling_out_contact_details(contact)
        # submit the new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_from_group(self, group, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text(group)
        wd.find_element_by_id(id).click()
        wd.find_element_by_name("remove").click()
        self.return_to_home_page()
        self.contact_cache = None

    def add_contact_to_group(self, group, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_id(id).click()
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group)
        wd.find_element_by_name("add").click()
        self.return_to_home_page()
        self.contact_cache = None


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            self.app.open_home_page()

    def modify_first(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.click_to_edit_contact(index)
        self.filling_out_contact_details(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        self.click_to_edit_contact_by_id(id)
        self.filling_out_contact_details(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def click_to_edit_contact(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name('a').click()

    def click_to_edit_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="edit.php?id='+id+'"]').click()

    def filling_out_contact_details(self, contact):
        self.update_contact_field_value("firstname", contact.firstname)
        self.update_contact_field_value("middlename", contact.middlename)
        self.update_contact_field_value("lastname", contact.lastname)
        self.update_contact_field_value("nickname", contact.nickname)
        self.update_contact_field_value("address", contact.address)
        self.update_contact_field_value("home", contact.homephone)
        self.update_contact_field_value("mobile", contact.mobilephone)
        self.update_contact_field_value("work", contact.workphone)
        self.update_contact_field_value("phone2", contact.secondaryphone)
        self.update_contact_field_value("email", contact.email)
        self.update_contact_field_value("email2", contact.email2)
        self.update_contact_field_value("email3", contact.email3)
        self.update_contact_by_select("bday", contact.bday)
        self.update_contact_by_select("bmonth", contact.bmonth)
        self.update_contact_field_value("byear", contact.byear)
        self.update_contact_by_select("new_group", contact.group_name)

    def update_contact_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def update_contact_by_select(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                column = element.find_elements_by_tag_name("td")
                lastname = column[1].text
                firstname = column[2].text
                id = column[0].find_element_by_name('selected[]').get_attribute("value")
                address = column[3].text
                #here we take all emails
                email = column[4].text
                allphones = column[5].text
                self.contact_cache.append(Contact(firstname=firstname,
                                                  lastname=lastname,
                                                  id=id,
                                                  address=address,
                                                  email=email,
                                                  all_phones_from_home_page=allphones))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name('a').click()

    def open_contact_to_edit_by_index(self, index):
        self.open_contact_page()
        self.click_to_edit_contact(index)

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        middlename = wd.find_element_by_name('middlename').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        homephone = wd.find_element_by_name('home').get_attribute("value")
        workphone = wd.find_element_by_name('work').get_attribute("value")
        mobilephone = wd.find_element_by_name('mobile').get_attribute("value")
        secondaryphone = wd.find_element_by_name('phone2').get_attribute("value")
        address = wd.find_element_by_name('address').get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        wd.find_element_by_name('phone2').get_attribute("value")
        return Contact(firstname=firstname,
                       lastname=lastname,
                       id=id,
                       middlename=middlename,
                       address=address,
                       homephone=homephone,
                       workphone=workphone,
                       mobilephone=mobilephone,
                       secondaryphone=secondaryphone,
                       email=email,
                       email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)

        print("##########")
        print(homephone)
        return Contact(homephone=homephone,
                       workphone=workphone,
                       mobilephone=mobilephone,
                       secondaryphone=secondaryphone)

    # def get_contact_from_view_page_edited(self, index):
    #     wd = self.app.wd
    #     self.open_contact_view_by_index(index)
    #     text = wd.find_element_by_id("content").text
    #     print("################")
    #     for element in wd.find_elements_by_na("entry"):
    #     print("".join(filter(lambda x: x != "", map(lambda x: self.clear(x), text))))

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        print(text)
        return text








