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
heading_catalog = "xpath,//title[text()='All Courses & Tutorials | Codecademy']"
course_path = "xpath,//A[text()='%s']"

# Locators for codecademy course page(codecademy_course_page.py)
heading_course = "xpath,//title[text() = '%s']"
recommended_path= "xpath,//H2[text() = 'Recommended']"
recommeded_course_sql_path = "xpath,//a[@href='/learn/learn-sql'][@data-testid='curriculum-card-learn-sql']"


# Locators for codecademy enroll course page(codecademy_enroll_course_page.py)
heading_learn_sql = "xpath,//title[text() = '%s']"
enroll_course_button = "xpath,//header/descendant::A[@aria-label='Start Course'][text()='Start']"
