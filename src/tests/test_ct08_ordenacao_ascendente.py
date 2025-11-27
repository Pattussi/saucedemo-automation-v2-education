import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.ordenacao
@pytest.mark.regressao

class TestCT08:
    def test_ct08_ordenacao_ascendente(self):
        login_page = LoginPage()
        home_page = HomePage()


        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.aplicar_filtro_ascendente()

        assert home_page.produtos_em_ordem_ascendente(), "Os produtos não estão ordenados corretamente."

