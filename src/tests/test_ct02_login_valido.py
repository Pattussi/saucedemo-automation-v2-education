import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke

class Testct02:
    def test_ct02_login_valido(self):
        
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.fazer_login("standard_user", "secret_sauce")
        
        home_page.verificar_login_com_sucesso()