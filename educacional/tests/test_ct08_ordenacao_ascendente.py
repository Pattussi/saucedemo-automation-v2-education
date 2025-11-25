import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

# Este teste valida a ordenação alfabética dos produtos:
# Login -> aplicar filtro A-Z -> validar ordenação

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.ordenacao
class TestCT08:
    def test_ct08_ordenacao_ascendente(self):
        login_page = LoginPage()
        home_page = HomePage()

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Sem POM ---
        # conftest.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID,"login-button").click()

        # ------------------- APLICAR FILTRO A-Z -------------------
        home_page.aplicar_filtro_ascendente()

        # --- Sem POM ---
        # select = Select(conftest.driver.find_element(By.CLASS_NAME,"product_sort_container"))
        # select.select_by_value("az")

        # ------------------- VALIDAR ORDEM -------------------
        assert home_page.produtos_em_ordem_ascendente(), "Os produtos não estão ordenados corretamente."

        # --- Sem POM ---
        # nomes = [el.text for el in conftest.driver.find_elements(By.CLASS_NAME,"inventory_item_name")]
        # assert nomes == sorted(nomes)
