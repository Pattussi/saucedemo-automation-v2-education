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
@pytest.mark.carrinho 
class TestCT06:
    def test_ct06_checkout_sem_preencher_campos(self):
        # Criamos instâncias das páginas necessárias (POM)
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        check_out_page = CheckOutPage() 
        texto_esperado = "Error: First Name is required"

        # ------------------- LOGIN -------------------
        login_page.fazer_login("standard_user", "secret_sauce")

        # --- Versão sem POM (antes) ---
        # conftest.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # conftest.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # conftest.driver.find_element(By.ID, "login-button").click()

        # ------------------- ADICIONAR 1º PRODUTO -------------------
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # --- Versão sem POM (antes) ---
        # conftest.driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        # conftest.driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        # ------------------- VALIDAR PRODUTO NO CARRINHO -------------------
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")

        # --- Versão sem POM (antes) ---
        # conftest.driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()
        # assert conftest.driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # ------------------- CHECKOUT -------------------
        carrinho_page.clicar_botao_check_out()
        check_out_page.preencher_check_out("", "Pattussi", "12345")
       
        # --- Versão sem POM (antes) ---
        # conftest.driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()
        # conftest.driver.find_element(By.ID, "last-name").send_keys("Pattussi")
        # conftest.driver.find_element(By.ID, "postal-code").send_keys("12345")
        # conftest.driver.find_element(By.XPATH, "//input[@class='btn_primary cart_button']").click()

        # # ------------------- VALIDAR MENSAGEM DE ERRO -------------------
        check_out_page.verificar_texto_error(texto_esperado)
        # # assert conftest.driver.find_element(By.XPATH,"//*[@id='checkout_info_container'/div/form/h3 and text()='Error: First Name is required']").is_displayed()


       