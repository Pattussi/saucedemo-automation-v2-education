import pytest
import conftest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# Este teste cobre o cenário de login inválido.
# O objetivo é validar a mensagem de erro exibida
# quando o usuário insere credenciais incorretas.

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.negativo

class TestCT03:
    def test_ct03_login_invalido(self):
        mensagem_de_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
        
        # Instancia a página de login
        login_page = LoginPage()
        
        # ------------------- LOGIN INVÁLIDO -------------------
        login_page.fazer_login("standard_user", "12345678")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- VALIDA MENSAGEM DE ERRO -------------------
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_de_erro_esperada)

        # --- Versão sem POM ---
        # mensagem_erro = conftest.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        # assert mensagem_erro == mensagem_de_erro_esperada

        print("Teste finalizado com sucesso")
