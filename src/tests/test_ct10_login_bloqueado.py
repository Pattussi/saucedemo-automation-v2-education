import pytest
import conftest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.negativo

class TestCT10:
    def test_ct10_login_bloqueado(self):
        driver = conftest.driver
        login_page = LoginPage(driver)
        mensagem_esperada = "Epic sadface: Sorry, this user has been locked out."

 
        login_page.fazer_login("locked_out_user", "secret_sauce")
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_esperada)
