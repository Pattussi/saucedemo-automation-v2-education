import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
from pages.check_out_page import CheckOutPage
from pages.finish_page import FinishPage
from selenium.webdriver.common.by import By

# Este teste cobre o fluxo completo de compra:
# Login -> adicionar produtos -> validar carrinho -> checkout -> finalizar compra

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.checkout
@pytest.mark.negativo
@pytest.mark.formulario

class TestCT06:
    def test_ct06_checkout_sem_preencher_campos(self):
        driver = conftest.driver
        # Criamos instâncias das páginas necessárias (POM)
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        carrinho_page = CarrinhoPage(driver)
        check_out_page = CheckOutPage(driver) 
        texto_esperado = "Error: First Name is required"

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

        # ------------------- CHECKOUT -------------------
        carrinho_page.clicar_botao_check_out()
        check_out_page.preencher_check_out("", "Pattussi", "12345")
       
        # --- Versão sem POM ---
        # conftest.driver.find_element(By.ID, "checkout").click()
        # conftest.driver.find_element(By.ID, "first-name").send_keys("")
        # conftest.driver.find_element(By.ID, "last-name").send_keys("Pattussi")
        # conftest.driver.find_element(By.ID, "postal-code").send_keys("12345")
        # conftest.driver.find_element(By.ID, "continue").click()

        # # ------------------- VALIDAR MENSAGEM DE ERRO -------------------
        check_out_page.verificar_texto_error(texto_esperado)

        # --- Versão sem POM ---
        # # assert conftest.driver.find_element(By.XPATH,"//*[@class='error-message-container error']").is_displayed()


       