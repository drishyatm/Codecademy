# Common locator file for all locators


############################################
# Selectors we can use
# ID
# NAME
# css selector
# CLASS_NAME
# LINK_TEXT
# PARTIAL_LINK_TEXT
# XPATH
###########################################

# Locators for the login_page

username = "xpath,//INPUT[@id='user_login']"
password = "xpath,//INPUT[@id='login__user_password']"
login_button = "xpath,//BUTTON[@id='user_submit']"

# Locators for codecademy home page(codecademy_home_page.py)
heading = "xpath,//title[text()='Dashboard | Codecademy']"
catalog_path = "xpath,//A[text()='Catalog']"
search_icon = "xpath,//BUTTON[@data-testid='header-search']"
search_type_text_area = "xpath,//input[@name='query']"
popular_search_area = "xpath,//BUTTON[text()='%s']"
search_redirect_page_check = "xpath,//div//span[text()='1']"

# Locators for codecademy catalog page(codecademy_catalog_page.py)
heading_catalog = "xpath,//title[text()='Catalog Home | Codecademy']"
course_path = "xpath,//A[text()='%s']"

# Locators for codecademy course page(codecademy_course_page.py)
heading_course = "xpath,//title[text() = '%s']"
recommended_path= "xpath,//H2[text() = 'Recommended']"
recommeded_course_path = "xpath,//a[@data-testid='%s']"


# Locators for codecademy enroll course page(codecademy_enroll_course_page.py)
heading_enroll_page = "xpath,//title[text() = '%s']"
enroll_course_button = "xpath,//A[@data-testid='syllabus-header-cta-button'][text()='Start']"

#Locators for start course page (codecademy_start_course_page.py)
heading_start_page = "xpath,//title[text() = '%s']"
scroll_element = "xpath,//div//descendant::p[text()='Press Run.']"
code_element = "xpath,//code//descendant::div[@class ='CodeMirror'] "
code_area = "xpath,//div[@class='view-line']//descendant::span"
run_button = "xpath,//button[text()='Run']"

