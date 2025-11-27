import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# Este teste valida o comportamento do login bloqueado:
# Tentar login -> verificar mensagem de usuário bloqueado

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.negativo

class TestCT10:
    def test_ct10_login_bloqueado(self):
        login_page = LoginPage()
        mensagem_esperada = "Epic sadface: Sorry, this user has been locked out."

        # ------------------- LOGIN -------------------
        login_page.fazer_login("locked_out_user", "secret_sauce")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- VALIDAR MENSAGEM -------------------
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_esperada)
        
        # --- Versão sem POM ---
        # erro = conftest.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        # assert erro == mensagem_esperada
