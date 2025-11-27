import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
from pages.check_out_page import CheckOutPage
from pages.finish_page import FinishPage
from selenium.webdriver.common.by import By

# Este teste cobre o fluxo completo de compra:
# Login -> adicionar produtos -> validar carrinho -> checkout -> finalizar compra

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.regressao
@pytest.mark.fluxo_completo

class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        # Criamos instâncias das páginas necessárias (POM)
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        check_out_page = CheckOutPage() 
        finish_page = FinishPage()
        texto_esperado = "Thank you for your order!"

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- ADICIONAR 1º PRODUTO -------------------
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Backpack']").click()
        # conftest.driver.find_element(By.ID, "add-to-cart").click()

        # ------------------- VALIDAR PRODUTO NO CARRINHO -------------------
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()
        # assert conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Backpack']").is_displayed()

        # ------------------- ADICIONAR 2º PRODUTO -------------------
        carrinho_page.clicar_continuar_comprando()
        home_page.adicionar_ao_carrinho("Sauce Labs Bike Light")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "continue-shopping").click()
        # conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Bike Light']").click()
        # conftest.driver.find_element(By.ID, "add-to-cart").click()

        # ------------------- VALIDAR 2 PRODUTOS NO CARRINHO -------------------
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Bike Light")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()
        # assert conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Backpack']").is_displayed()
        # assert conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Bike Light']").is_displayed()

        # ------------------- CHECKOUT -------------------
        carrinho_page.clicar_botao_check_out()
        check_out_page.preencher_check_out("Leonardo", "Pattussi", "12345")

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "checkout").click()
        # conftest.driver.find_element(By.ID, "first-name").send_keys("Leonardo")
        # conftest.driver.find_element(By.ID, "last-name").send_keys("Pattussi")
        # conftest.driver.find_element(By.ID, "postal-code").send_keys("12345")
        # conftest.driver.find_element(By.ID, "continue").click()

        # ------------------- VALIDAR PRODUTOS NA FINALIZAÇÃO -------------------
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Bike Light")

        # --- Versão sem POM ---
        # assert conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Backpack']").is_displayed()
        # assert conftest.driver.find_element(By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='Sauce Labs Bike Light']").is_displayed()

        # ------------------- FINALIZAR COMPRA -------------------
        check_out_page.finalizar_compra()
        finish_page.verificar_texto_compra_finalizada(texto_esperado)

        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "finish").click()
        # assert conftest.driver.find_element(By.XPATH,"//h2[@class='complete-header' and text()='Thank you for your order!']").is_displayed()
