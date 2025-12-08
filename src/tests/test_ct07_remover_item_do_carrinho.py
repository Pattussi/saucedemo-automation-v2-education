import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.regressao

class TestCT07:
    def test_ct07_remover_item_do_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        carrinho_page = CarrinhoPage(driver)


        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        home_page.acessar_carrinho()

        carrinho_page.remover_item_do_carrinho("Sauce Labs Backpack")

        carrinho_page.verificar_produto_nao_existe("Sauce Labs Backpack")
