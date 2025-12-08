import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.ordenacao
@pytest.mark.regressao

class TestCT05:
    def test_ct05_ordenacao_produtos_preco(self):
        driver = conftest.driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        
        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.aplicar_filtro_decrescente()

        assert home_page.precos_em_ordem_decrescente()
