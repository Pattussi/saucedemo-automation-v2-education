import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope="function")
def setup_teardown():
    global driver

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.saucedemo.com/")
    
    yield
    
    driver.quit()
