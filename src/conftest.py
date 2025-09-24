import pytest
from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    global driver 
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")
    yield
    driver.quit()