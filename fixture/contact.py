from selenium.webdriver.support.ui import Select


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

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def open_contact_page(self):
        wd = self.app.wd
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
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)

    def update_contact_by_select(self, field_name, value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)






