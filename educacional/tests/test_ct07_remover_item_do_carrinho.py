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

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- ADICIONAR ITEM -------------------
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Backpack']").click()
        # conftest.driver.find_element(By.ID, "add-to-cart").click()

        # ------------------- ACESSAR CARRINHO -------------------
        home_page.acessar_carrinho()

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()

        # ------------------- REMOVER ITEM -------------------
        carrinho_page.remover_item_do_carrinho("Sauce Labs Backpack")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        # ------------------- VALIDAR REMOÇÃO -------------------
        carrinho_page.verificar_produto_nao_existe("Sauce Labs Backpack")

        # --- Versão sem POM ---
        # assert len(conftest.driver.find_elements(By.XPATH,"//div[text()='Sauce Labs Backpack']")) == 0