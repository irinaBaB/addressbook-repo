#from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, baseurl):
        if browser =='chrome':
            self.wd = webdriver.Chrome('/Users/irinapirandello/Documents/Courses/python-testing_course_rus/chromedriver')
            #the way below stopped working
            #self.wd = webdriver.Chrome(ChromeDriverManager().install())
        elif browser =='firefox':
            self.wd = webdriver.Firefox()
        else:
            raise ValueError(f"Unrecognised browser {browser}")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseurl = baseurl

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

