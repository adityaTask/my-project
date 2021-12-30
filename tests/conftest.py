import pytest
from base.web_driver import WebDriver

@pytest.fixture(scope="class")
def one_time_setup(request,browser):
    print("Running one time setup")
    wd = WebDriver(browser)
    driver = wd.web_driver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")