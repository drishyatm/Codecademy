

--------
A Pythonic Selenium automation framework
--------
You can use this test automation framework to write:

1. __Selenium__ and Python automation scripts to test web applications



&nbsp;


This GUI and API test automation framework is developed and maintained by [Qxf2 Services](https://qxf2.com). This framework is written in __Python__ and is based on the __Page Object Model__ - a design pattern that makes it easy to maintain and develop robust tests. We have also included our __API test automation framework__ based on the player-interface pattern in this repository. You can now write your API tests along with your Selenium and Appium tests.

Here we've implemented version of this framework at Codecademy . In all cases, this framework helped us write automated tests within the first week of our engagement. We hope you find this framework useful too!



------
Setup
------

The setup for our open-sourced Python test automation framework is fairly simple. Don't get fooled by the length of this section. We have documented the setup instructions in detail so even beginners can get started.

The setup has 2 parts:

1. Prerequisites
2. Setup for GUI/Selenium automation


__1. Prerequisites__

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

c) If you do not have it already, get pip (NOTE: Most recent Python distributions come with pip)

d) pip install -r requirements.txt to install dependencies

e) Add a page, login_page_conf.py to conf with your credentials 




__2. Setup for GUI/Selenium automation__


a) Get setup with your browser driver. If you don't know how to, please try:

   > [For Chrome](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

   > [For Firefox]( https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver)

#Note: Check Firefox version & Selenium version compatibility before downloading geckodriver.

__If your setup goes well__, you should be to run a simple test with this command:

1. Chrome: `python -m pytest -k example_form -B Chrome`

2. Firefox: `python -m pytest -k example_form -B Firefox`

-------------------
Repository details
-------------------
a) Directory structure of our current Templates

   ./

	|__conf: For all configurations and credential files

	|__log: Log files for all tests

	|__page_objects: Contains our Base Page, different Page Objects, DriverFactory, PageFactory

	|__endpoints: Contains our Base Mechanize, different End Points, API Player, API Interface

	|__screenshots: For screen shots

	|__tests: Put your tests in here

	|__utils: All utility modules (email_util,TestRail, BrowserStack, Base Logger, post_test_reports_to_slack) are kept in this folder


---------------------------
COMMANDS FOR RUNNING TESTS
---------------------------
python -m pytest -k test_codecademy.py  ( Enrolling for the course)
python -m pytest -k test_search_course.py (Searching for course)

python -m pytest -k test_codecademy.py --browser headless-chrome ( without launching browser)





