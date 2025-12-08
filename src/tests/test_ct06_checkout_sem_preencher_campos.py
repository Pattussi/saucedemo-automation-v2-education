import pytest
import conftest 
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
from pages.check_out_page import CheckOutPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.checkout
@pytest.mark.negativo
@pytest.mark.formulario

class TestCT06:
    def test_ct06_checkout_sem_preencher_campos(self):
        driver = conftest.driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        carrinho_page = CarrinhoPage(driver)
        check_out_page = CheckOutPage(driver) 
        texto_esperado = "Error: First Name is required"

 
        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")

        carrinho_page.clicar_botao_check_out()
        check_out_page.preencher_check_out("", "Pattussi", "12345")
       
        check_out_page.verificar_texto_error(texto_esperado)
  


       