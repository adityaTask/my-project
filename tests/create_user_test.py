import time
import unittest
import pytest
from pages.home.login_page import LoginPage
from pages.users.create_user import CreateUser

@pytest.mark.usefixtures("one_time_setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,one_time_setup):
        self.lp = LoginPage(self.driver)
        self.cu = CreateUser(self.driver)


    @pytest.mark.run(order=1)
    def test_login(self):
        self.lp.login()
        time.sleep(3)
        result = self.lp.verify_login()
        assert result == True

    @pytest.mark.run(order=2)
    def test_create_user(self):
        self.cu.create_user("ADITYA","Admin@123","Aditya","Singh","Hexagon","PPM","123")
        result = self.cu.verify_user_created("ADITYA")
        assert result == True