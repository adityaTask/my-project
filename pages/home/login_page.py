from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _user_name = "P101_USERNAME"
    _password = "P101_PASSWORD"
    _login_button = "P101_LOGIN"
    _home = "//a[text()='Home']"

    def enter_user_name(self,user_name):
        self.send_keys(data=user_name,locator=self._user_name)

    def enter_password(self,password):
        self.send_keys(data=password,locator=self._password)

    def click_login_button(self):
        self.element_click(locator=self._login_button)

    def login(self,user_name="SPRDSDB",password = "Admin@123"):
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.click_login_button()

    def verify_login(self):
        return self.is_element_present(locator=self._home,locatorType="xpath")

