import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage



@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.regressao

class TestCT09:
    def test_ct09_validar_quantidade_itens_no_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        carrinho_page = CarrinhoPage(driver)


        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")
        home_page.acessar_carrinho()
        carrinho_page.clicar_continuar_comprando()
        home_page.adicionar_ao_carrinho("Sauce Labs Bike Light")
        home_page.acessar_carrinho()
        quantidade = carrinho_page.obter_quantidade_itens()
        assert quantidade == 2, f"Esperado 2 itens, porém havia {quantidade}"
        

