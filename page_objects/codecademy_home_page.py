"""
This class models the redirect page of the Selenium tutorial
URL: learn
The Catalog would be there to select the course. 
We can also search the course by typing the course name or pick any from the popular search.

"""

import conf.locators_conf as locators
import conf.test_codecademy_conf as conf
from utils.Wrapit import Wrapit
from .Base_Page import Base_Page

class Codecademy_Home_Page(Base_Page):
    "Page object for the Codecademy Home page"

    # locators
    heading = locators.heading
    catalog_path = locators.catalog_path
    redirect_title_catalog = conf.redirect_title_catalog
    #locator for the search course 
    search_icon = locators.search_icon
    search_type_text_area = locators.search_type_text_area
    search_redirect_page_check = locators.search_redirect_page_check
    redirect_title_search = conf.redirect_title_search
    popular_search_area = locators.popular_search_area
    course_name = conf.course_name_popular

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'learn'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading_home(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading)
        self.conditional_write(result_flag,
                               positive='Heading present on Home page',
                               negative='Heading on Homepage is not matching!!',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_catalog(self):
        "Click the catalog in home page"
        result_flag = self.click_element(self.catalog_path)
        self.conditional_write(result_flag,
                               positive='Clicked on the catalog on home page',
                               negative='Could not click on the catalog on home page',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_catalog(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.redirect_title_catalog in self.driver.title:
            result_flag = True
            self.switch_page("Catalog page")
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_search_bar(self):
        "Click on the search bar"
        result_flag = self.click_element(self.search_icon)
        self.conditional_write(result_flag,
                               positive='Clicked on the Search bar on home page',
                               negative='Could not click on the Search bar on home page',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_search_course(self, search_text_course):
        "Type the course in seach bar"
        result_flag = self.set_text(self.search_type_text_area, search_text_course)
        self.conditional_write(result_flag,
                               positive='Set the course_name to: %s' % search_text_course,
                               negative='Failed to set the name in the search bar',
                               level='debug')

        return result_flag

    def search_course_enter(self):
        "Hit enter inorder to search"
        result_flag = self.hit_enter(self.search_type_text_area)
        self.conditional_write(result_flag,
                               positive='Hit the enter',
                               negative='Failed to hit the enter after the search bar',
                               level='debug')

        return result_flag

    def verify_title_search(self):
       "Check if we have been redirected to the redirect page"
       result_flag = False
       if self.redirect_title_search in self.driver.title:
           result_flag = True

       return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_popular_search(self):
        "Click on the Popular search options "
        result_flag = self.click_element(self.popular_search_area%self.course_name)
        self.conditional_write(result_flag,
                               positive='Clicked on the Popular search options on home page',
                               negative='Could not click on the Search bar on home page',
                               level='debug')

        return result_flag

    def verify_course_list(self):
        "Verifying the courses are displayed as per search"
        result_flag = self.check_element_present(self.search_redirect_page_check)
        self.conditional_write(result_flag,
                               positive='List of courses Displayed on the Home page',
                               negative='No courses selected for %s!'%self.course_name,
                               level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def go_to_catalog(self):
        "Click  the Catalog page"
        result_flag = self.check_heading_home()
        result_flag &= self.click_catalog()
        result_flag &= self.check_redirect_catalog()
        
        return result_flag

    @Wrapit._exceptionHandler
    def search_course(self, search_text_course):
        "Click the search and enter the course name and search for it"
        result_flag = self.click_search_bar()
        result_flag &= self.set_search_course(search_text_course)
        result_flag &= self.search_course_enter()
        result_flag &= self.verify_title_search()
        result_flag &= self.verify_course_list()
        result_flag &= self.click_search_bar()
        result_flag &= self.select_popular_search()
        result_flag &= self.verify_title_search()
        result_flag &= self.verify_course_list()

        return result_flag  
