import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
from pages.check_out_page import CheckOutPage
from pages.finish_page import FinishPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.regressao
@pytest.mark.fluxo_completo

class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        check_out_page = CheckOutPage() 
        finish_page = FinishPage()
        texto_esperado = "Thank you for your order!"

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")

        carrinho_page.clicar_continuar_comprando()

        home_page.adicionar_ao_carrinho("Sauce Labs Bike Light")

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Bike Light")
        
        carrinho_page.clicar_botao_check_out()

        check_out_page.preencher_check_out("Leonardo", "Pattussi", "12345")

        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Bike Light")

        check_out_page.finalizar_compra()
        finish_page.verificar_texto_compra_finalizada(texto_esperado)