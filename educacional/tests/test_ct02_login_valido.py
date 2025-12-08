import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

# Este teste cobre o cenário de login válido.
# Valida se o sistema permite o acesso à HomePage com sucesso.

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class Testct02:
    def test_ct02_login_valido(self):
        # Instancia as páginas necessárias
        driver = conftest.driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        
        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- VALIDAÇÃO -------------------
        home_page.verificar_login_com_sucesso()

        # --- Versão sem POM ---
        # assert conftest.driver.find_element(By.XPATH, "//div[@class='app_logo']").is_displayed()
