"""
This Page is for the SQL course 
URL: catalog/language/sql
This page consists of the list of SQL courses for which we select the recommended SQL course
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
import conf.course_page_conf as course_page_conf
from utils.Wrapit import Wrapit


class Codecademy_Course_Page(Base_Page):
    "Page Object for the Course page"

    # locators
    heading_course_sql = locators.heading_course_sql
    course_heading = course_page_conf.course_heading
    recommended_path_sql = locators.recommended_path_sql
    recommeded_course_sql_path = locators.recommeded_course_sql_path
    redirect_title_course = course_page_conf.redirect_title_course

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'catalog/language/sql'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(
            self.heading_course_sql % self.course_heading)
        self.conditional_write(result_flag,
                               positive='heading present on %s page'%self.course_heading,
                               negative='Heading on %s Page is INCORRECT!!'%self.course_heading,
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_recommended(self):
        " Click the SQL course in catalog page"
        result_flag = self.check_element_present(self.recommended_path_sql)
        self.conditional_write(result_flag,
                               positive='Verified the Recommended course is %s'%self.redirect_title_course,
                               negative='Could not verify the Recommeded course ',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_course(self):
        "Click the  course in  Course page"
        result_flag = self.click_element(self.recommeded_course_sql_path)
        self.conditional_write(result_flag,
                               positive='Clicked on the %s in the course'%self.redirect_title_course,
                               negative='Could not click on the recommended course %s'%self.redirect_title_course,
                               level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if we have been redirected to the Recommended course page"
        result_flag = False
        if self.redirect_title_course in self.driver.title:
            result_flag = True
            self.switch_page("Recommended course page")

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_course_sql(self):
        "Selecting the course"
        result_flag = self.check_heading()
        result_flag &= self.check_recommended()
        result_flag &= self.click_course()
        result_flag &= self.check_redirect()

        return result_flag
