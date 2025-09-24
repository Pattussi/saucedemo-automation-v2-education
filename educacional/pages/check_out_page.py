import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# A CheckOutPage representa a tela onde o usuário preenche seus dados pessoais
# antes de finalizar a compra.

class CheckOutPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver  
        # Localizadores dos campos do formulário
        self.first_name_check_out = (By.ID, "first-name")
        self.last_name_check_out = (By.ID, "last-name")
        self.postal_code_check_out = (By.ID, "postal-code")
        self.botao_continue_check_out = (By.XPATH, "//input[@class='btn_primary cart_button']")
        self.botao_finish = (By.XPATH, "//a[@class='btn_action cart_button']")
       
    def preencher_check_out(self, first_name, last_name, zip_code):
        # Preenche o formulário com os dados do cliente
        self.escrever(self.first_name_check_out, first_name)
        self.escrever(self.last_name_check_out, last_name)
        self.escrever(self.postal_code_check_out, zip_code)
        self.clicar(self.botao_continue_check_out)

    def finalizar_compra(self):
        # Clica no botão "Finish" para concluir a compra
        self.clicar(self.botao_finish)
