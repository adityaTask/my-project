from base.selenium_driver import SeleniumDriver

class NavigationPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _administration = "//h3[text()='Administration']"
    _global_setup = "//h3[contains(text(),'Global Setup')]"
    _users = "//span[contains(text(),'Users')]"

    def navigate_to_administration(self):
        self.element_click(locator=self._administration,locator_type="xpath")

    def navigate_to_global_setup(self):
        self.element_click(locator=self._global_setup,locator_type="xpath")

    def navigate_to_users(self):
        self.element_click(locator=self._users,locator_type="xpath")


