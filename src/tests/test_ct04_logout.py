import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.logout
class TestCT04:
    def test_ct04_logout(self):
        login_page = LoginPage()
        home_page = HomePage()
        base_page = BasePage()  
        

        login_page.fazer_login("standard_user", "secret_sauce")
        
        home_page.fazer_logout()
        
        base_page.verificar_se_elemento_existe(login_page.login_button)

