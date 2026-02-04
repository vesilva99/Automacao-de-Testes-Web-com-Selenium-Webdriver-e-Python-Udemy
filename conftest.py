import pytest
from selenium import webdriver



driver: webdriver.Remote


@pytest.fixture(scope="function")
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield driver

    # teardown
    driver.quit()