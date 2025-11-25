import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage

# Este teste valida a contagem de itens no carrinho:
# Login -> adicionar 2 itens -> validar quantidade

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT09:
    def test_ct09_validar_quantidade_itens_no_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Sem POM ---
        # conftest.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID,"login-button").click()


        # ------------------- ADICIONAR ITENS -------------------
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")
        home_page.acessar_carrinho()
        carrinho_page.clicar_continuar_comprando()
        home_page.adicionar_ao_carrinho("Sauce Labs Bike Light")

        # --- Sem POM (antes) ---
        # conftest.driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()
        # assert conftest.driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        # conftest.driver.find_element(By.XPATH, "//a[@class='btn_secondary']").click()
        # conftest.driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        # conftest.driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        # ------------------- ACESSAR CARRINHO -------------------
        home_page.acessar_carrinho()
        # --- Sem POM (antes) ---
        # conftest.driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()

        # ------------------- VALIDAR CONTAGEM -------------------
        quantidade = carrinho_page.obter_quantidade_itens()
        assert quantidade == 2, f"Esperado 2 itens, porém havia {quantidade}"
        
        # --- Sem POM ---
        # itens = conftest.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        # assert len(itens) == 2
