from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_link_text("groups").click()
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test1")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("one test")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("second field")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
