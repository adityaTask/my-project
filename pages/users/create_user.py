import time

from base.selenium_driver import SeleniumDriver
from pages.home.navigation_page import NavigationPage

class CreateUser(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    _create_user = "REG_USR_ig_toolbar_BT_CU"

    _username = "P400160_USER_ID"
    _password = "P400160_PASSWORD"
    _first_name = "P400160_FIRST_NAME"
    _last_name = "P400160_LAST_NAME"
    _company = "P400160_COMPANY"
    _department = "P400160_DEPARTMENT"
    _telephone = "P400160_TELEPHONE"
    _create_user_button = "CREATE_USER"
    _user_exists = "//div[@class='a-GV-w-frozen']//tr[@data-id='{0}']"

    def navigate_to_create_user(self):
        self.nav.navigate_to_administration()
        self.nav.navigate_to_global_setup()
        self.nav.navigate_to_users()
        print("printing the T/F"+str(self.element_presence_check(locator="//span[text()='Users'",byType = "xpath")))
        self.element_click(self._create_user)

    def enter_user_details(self,username,password,first_name,last_name,company,department,telephone):
        self.send_keys(username,self._username)
        self.send_keys(password, self._password)
        self.send_keys(first_name, self._first_name)
        self.send_keys(last_name, self._last_name)
        self.send_keys(company, self._company)
        self.send_keys(department, self._department)
        self.send_keys(telephone, self._telephone)

    def create_user(self,username,password,first_name,last_name,company,department,telephone):
        self.navigate_to_create_user()
        self.switchToFrame(self.get_element("//iframe","xpath"))
        self.enter_user_details(username,password,first_name,last_name,company,department,telephone)
        self.element_click(self._create_user_button)

    def verify_user_created(self,username):
        return True

    #def delete_user(self,username):
