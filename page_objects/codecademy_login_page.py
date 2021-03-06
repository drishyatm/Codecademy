"""
This class models the codecademy login page.
URL: login
"""
from .Base_Page import Base_Page
from .codecademy_login_page_object import Codecademy_Login_Page_Object
import conf.test_codecademy_conf as conf

class Codecademy_Login_Page(Base_Page, Codecademy_Login_Page_Object):
    "Page Object for the Codecademy Login page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = conf.login_url
        print("launching the Login page")
        self.open(url)
