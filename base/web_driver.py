from selenium import webdriver


class WebDriver():

    def __init__(self, browser):
        self.browser = browser

    def web_driver_instance(self):

        baseURL = "https://in-srddb.ingrnet.com:8443/apex/sdb123/f?p=101:LOGIN::::::"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseURL)
        return driver

