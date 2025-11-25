import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT07:
    def test_ct07_remover_item_do_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- ADICIONAR ITEM -------------------
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # --- Sem POM ---
        # conftest.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
        # conftest.driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        # ------------------- ACESSAR CARRINHO -------------------
        home_page.acessar_carrinho()

        # ------------------- REMOVER ITEM -------------------
        carrinho_page.remover_item_do_carrinho("Sauce Labs Backpack")

        # --- Sem POM ---
        # conftest.driver.find_element(By.XPATH, "//button[text()='REMOVE']").click()

        # ------------------- VALIDAR REMOÇÃO -------------------
        carrinho_page.verificar_produto_nao_existe("Sauce Labs Backpack")

        # --- Versão sem POM (antes) ---
        # assert len(conftest.driver.find_elements(By.XPATH,"//div[text()='Sauce Labs Backpack']")) == 0