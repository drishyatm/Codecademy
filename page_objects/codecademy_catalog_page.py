"""
This class models the Catalog page for Codecademy
URL: 'catalog/all'
The Catalog and list of all courses 
Select one of the course from the catalog
"""
from utils.Wrapit import Wrapit
from .Base_Page import Base_Page
import conf.locators_conf as locators
import conf.test_codecademy_conf as conf


class Codecademy_Catalog_Page(Base_Page):
    "Page Object for the Catalog page"

    # locators
    heading_catalog = locators.heading_catalog
    course_path = locators.course_path
    course_name = conf.course_name
    redirect_title_course = conf.redirect_title_course

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = conf.catalog_url
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading_catalog)
        self.conditional_write(result_flag,
                               positive='Heading present on Catalog page',
                               negative='Heading on Catalog page is not matching!!',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_course(self):
        "Click the course in catalog page"
        result_flag = self.click_element(
            self.course_path % self.course_name)
        self.conditional_write(result_flag,
                               positive='Clicked on the %s course' %self.course_name,
                               negative='Could not click on the %s course'%self.course_name,
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_redirect(self):
        "Check if we have been redirected to the course page"
        result_flag = False
        if self.redirect_title_course in self.driver.title:
            result_flag = True
            self.switch_page("Course page")

        return result_flag

    @Wrapit._exceptionHandler
    def select_course(self):
        "Selecting the course"
        result_flag = self.check_heading()
        result_flag &= self.click_course()
        result_flag &= self.check_redirect()

        return result_flag
