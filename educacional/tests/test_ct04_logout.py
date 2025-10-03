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
        
        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # ------------------- LOGOUT -------------------
        # Faz logout usando o POM
        home_page.fazer_logout()
            
        # Valida que voltou para tela de login
        base_page.verificar_se_elemento_existe(login_page.login_button)
        
        # --- Versão sem POM (antes) ---
        
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()
        # conftest.driver.find_element(By.ID, "react-burger-menu-btn").click()
        # conftest.driver.find_element(By.ID, "logout_sidebar_link").click()
        # assert conftest.driver.find_element(By.ID, "login-button").is_displayed()
