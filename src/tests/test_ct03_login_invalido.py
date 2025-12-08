import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.negativo

class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        
        mensagem_de_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
        
        login_page = LoginPage(driver)
        
        login_page.fazer_login("standard_user", "12345678")

        login_page.verificar_mensagem_erro_login_existe()

        login_page.verificar_texto_mensagem_erro_login(mensagem_de_erro_esperada)

        print("Teste finalizado com sucesso")