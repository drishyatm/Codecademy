"""
This Page is for the  course 
URL: catalog/language/<course>
This page consists of the list of courses for which we select the recommended course
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
import conf.test_codecademy_conf as conf
from utils.Wrapit import Wrapit


class Codecademy_Course_Page(Base_Page):
    "Page Object for the Course page"

    # locators
    heading_course = locators.heading_course
    course_heading = conf.course_heading
    recommended_path = locators.recommended_path
    recommeded_course_path = locators.recommeded_course_path
    recommended_course = conf.recommended_course
    redirect_title_course = conf.redirect_title_course_recommended

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = conf.course_url
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(
            self.heading_course % self.course_heading)
        self.conditional_write(result_flag,
                               positive='heading present on %s page'%self.course_heading,
                               negative='Heading on %s Page is INCORRECT!!'%self.course_heading,
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_recommended(self):
        " Check the  recommended course in catalog page"
        result_flag = self.check_element_present(self.recommended_path)
        self.conditional_write(result_flag,
                               positive='Verified the Recommended course is %s'%self.redirect_title_course,
                               negative='Could not verify the Recommeded course ',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_course(self):
        "Click the  course in  Course page"
        result_flag = self.click_element(self.recommeded_course_path %self.recommended_course)
        self.conditional_write(result_flag,
                               positive='Clicked on the %s in the course'%self.redirect_title_course,
                               negative='Could not click on the recommended course %s'%self.redirect_title_course,
                               level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    def check_redirect(self):
        "Check if we have been redirected to the Recommended course page"
        result_flag = False
        if self.redirect_title_course in self.driver.title:
            result_flag = True
            self.switch_page("Recommended course page")

        return result_flag

    @Wrapit._exceptionHandler
    def select_course_recommended(self):
        "Selecting the course"
        result_flag = self.check_heading()
        result_flag &= self.check_recommended()
        result_flag &= self.click_course()
        result_flag &= self.check_redirect()

        return result_flag
