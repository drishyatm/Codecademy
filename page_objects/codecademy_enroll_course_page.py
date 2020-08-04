"""
This class models the Codecademy page of the Enrolling the course 
URL: learn/learn-<course-name>
Verify the heading, click on start button of the course and verify the redirect
"""
from utils.Wrapit import Wrapit
import conf.locators_conf as locators
from .Base_Page import Base_Page
import conf.test_codecademy_conf as conf

class Codecademy_Enroll_Course_Page(Base_Page):
    "Page Object for the Enroll Course Page page"

    # locators
    heading_enroll_page = locators.heading_enroll_page
    enroll_course_button = locators.enroll_course_button
    enroll_heading =conf.enroll_heading
    redirect_title_course = conf.redirect_title_course_recommended

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = conf.enroll_url
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading_enroll_page %self.enroll_heading)
        self.conditional_write(result_flag,
                               positive='Heading present on Enroll Course page',
                               negative='Heading on Enroll Course Page is INCORRECT!!',
                               level='debug')

        return result_flag

   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_start_course(self):
        "Click the Start button in Recommended Course page"
        result_flag = self.click_element(self.enroll_course_button)
        self.conditional_write(result_flag,
                               positive='Clicked on the Start button  in the Enroll course page ',
                               negative='Could not click on the Start button Enroll course page',
                               level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    def check_redirect(self):
        "Check if we have been redirected to the Recommended course page"
        result_flag = False
        if self.redirect_title_course in self.driver.title:
            result_flag = True
            self.switch_page("Start course page")
         

        return result_flag

    @Wrapit._exceptionHandler
    def select_enroll_course(self):
        "Enroll for the course"
        result_flag = self.check_heading()
        result_flag &= self.click_start_course()
        #result_flag &= self.check_redirect()

        return result_flag
