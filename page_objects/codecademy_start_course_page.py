"""
This class models the Codecademy page of the Enrolling the course 
URL: courses/learn-sql/lessons/manipulation/exercises/<course>
Verify the heading, click on start button of the course and verify the redirect
"""
from utils.Wrapit import Wrapit
import conf.locators_conf as locators
from .Base_Page import Base_Page
import conf.test_codecademy_conf as conf


class Codecademy_Start_Course_Page(Base_Page):
    "Page Object for the Enroll Course Page page"

    # locators
    heading_start_page = locators.heading_start_page
    heading_connecting = conf.enroll_heading
    enroll_course_button = locators.enroll_course_button
    #redirect_title_course = 

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = conf.start_course_url
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading_start_page%self.heading_connecting)
        self.conditional_write(result_flag,
                               positive='Heading present on Start Course page',
                               negative='Heading on Start Course Page is not correct!!',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_start_course(self):
        "Click the Start button in Recommended Course page"
        result_flag = self.click_element(self.enroll_course_button)
        self.conditional_write(result_flag,
                               positive='Clicked on the Start button  in the   course page ',
                               negative='Could not click on the Start button   course page',
                               level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if we have been redirected to the Recommended course page"
        result_flag = False
        if self.redirect_title_course in self.driver.title:
            result_flag = True

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def learn_course(self):
        "Start  the course"
        result_flag = self.check_heading()
       # result_flag &= self.click_start_course()
        #result_flag &= self.check_redirect()

        return result_flag
