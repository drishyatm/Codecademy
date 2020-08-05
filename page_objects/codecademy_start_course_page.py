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
    scroll_path = locators.scroll_element
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
    def scroll_down_course(self):
        "Scroll down to start learning"
        print("In method of scroll down")
        result_flag = self.scroll_down(self.scroll_path)
        self.conditional_write(result_flag,
                               positive='Clicked on the Scroll in the   start page ',
                               negative='Could not scroll on the start course page',
                               level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    def check_redirect(self):
        "Check if we have been redirected to the Recommended course page"
        result_flag = False
        if self.redirect_title_course in self.driver.title:
            result_flag = True

        return result_flag

    @Wrapit._exceptionHandler
    def learn_course(self):
        "Start  the course"
        result_flag = self.check_heading()
        result_flag &= self.scroll_down_course()
       # result_flag &= self.click_start_course()
        #result_flag &= self.check_redirect()

        return result_flag
