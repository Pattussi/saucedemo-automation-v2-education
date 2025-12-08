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

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- APLICAR FILTRO (HIGH → LOW) -------------------
        home_page.aplicar_filtro_decrescente()

        # --- Versão sem POM ---
        # select = Select(conftest.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        # select.select_by_value("hilo")

        # ------------------- CAPTURAR LISTA DE PREÇOS -------------------
        # Aqui o método da HomePage já retorna os preços como números (floats)
        # e internamente aplica a lógica de comparação para validar a ordenação.
        
        assert home_page.precos_em_ordem_decrescente(), (
            "Os preços não estão ordenados corretamente do maior para o menor."
        )

        # --- Versão sem POM ---
        # precos = conftest.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        # valores = [float(p.text.replace("$","")) for p in precos]
        # assert valores == sorted(valores, reverse=True)
