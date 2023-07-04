from selenium.webdriver.support.ui import Select
from models.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.get("http://localhost/addressbook/")

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_create_contact_page()
        wd.find_element_by_name("theform").click()
        self.filling_out_contact_details(contact)
        # submit the new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("http://localhost/addressbook/index.php")

    def modify_first(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.filling_out_contact_details(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()

    def filling_out_contact_details(self, contact):
        self.update_contact_field_value("firstname", contact.firstname)
        self.update_contact_field_value("middlename", contact.middlename)
        self.update_contact_field_value("lastname", contact.lastname)
        self.update_contact_field_value("nickname", contact.nickname)
        self.update_contact_field_value("address", contact.address)
        self.update_contact_field_value("home", contact.homephone)
        self.update_contact_field_value("mobile", contact.mobilephone)
        self.update_contact_field_value("email", contact.email)
        self.update_contact_by_select("bday", contact.bday)
        self.update_contact_by_select("bmonth", contact.bmonth)
        self.update_contact_field_value("byear", contact.byear)

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


    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        list_c = []
        for element in wd.find_elements_by_name("entry"):
            rows = element.find_elements_by_tag_name("td")
            lastname = rows[1].text
            firstname = rows[2].text
            idc = rows[0].find_element_by_name('selected[]').get_attribute("value")
            list_c.append(Contact(firstname=firstname,lastname=lastname, idc=idc))
        return list_c


