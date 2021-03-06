"""
This class models the form on the Codecademy Login page
The form consists of some input fields username and password
"""
import conf.locators_conf as locators
import conf.test_codecademy_conf as conf
from utils.Wrapit import Wrapit


class Codecademy_Login_Page_Object:
    "Page object for the Login Page"

    # locators
    user_name_field = locators.username
    code_password = locators.password
    login_button = locators.login_button
    redirect_title = conf.redirect_title_home

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_user_name(self, user_name):
        "Set the user name on the form"
        result_flag = self.set_text(self.user_name_field, user_name)
        self.conditional_write(result_flag,
                               positive='Set the user_name to: %s' % user_name,
                               negative='Failed to set the name in the form',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self, password):
        "Set the email on the form"
        result_flag = self.set_text(self.code_password, password)
        self.conditional_write(result_flag,
                               positive='Set the password to: %s' % password,
                               negative='Failed to set the password in the form',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_login_button(self):
        "Click on 'Log in' button"
        result_flag = self.click_element(self.login_button)
        self.conditional_write(result_flag,
                               positive='Clicked on the "Login" button',
                               negative='Failed to click on "Login" button',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_redirect(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.redirect_title in self.driver.title:
            result_flag = True
            self.switch_page("Home page")

        return result_flag

    @Wrapit._exceptionHandler
    def Log_in(self, username, password):
        "Submit the Login page"
        result_flag = self.set_user_name(username)
        result_flag &= self.set_password(password)
        result_flag &= self.click_login_button()
        result_flag &= self.check_redirect()

        return result_flag
