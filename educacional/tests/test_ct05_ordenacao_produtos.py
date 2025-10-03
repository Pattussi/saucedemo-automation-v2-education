import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.ordenacao
class TestCT05:
    def test_ct05_ordenacao_produtos_preco(self):
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.fazer_login("standard_user", "secret_sauce")

        # ------------------- ORDENAR PRODUTOS -------------------
        home_page.aplicar_filtro_decrescente()

        # Captura os preços exibidos
        # Valida se a lista está em ordem crescente
        assert home_page.precos_em_ordem_decrescente()

        # --- Versão sem POM (antes) ---

        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()
        # conftest.driver.find_element(By.CLASS_NAME, "product_sort_container").send_keys("Price (low to high)")
        # precos = conftest.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        # valores = [float(p.text.replace("$", "")) for p in precos]
        # assert valores == sorted(valores)