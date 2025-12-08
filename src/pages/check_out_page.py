from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckOutPage(BasePage):

   
    def __init__(self, driver):
        super().__init__(driver)

        self.first_name_check_out = (By.ID, "first-name")
        self.last_name_check_out = (By.ID, "last-name")
        self.postal_code_check_out = (By.ID, "postal-code")
        self.botao_continue_check_out = (By.ID, "continue")
        self.botao_finish = (By.ID, "finish")
        self.check_out_message = (By.XPATH,"//*[@class='error-message-container error']")

    def preencher_check_out(self, first_name, last_name, zip_code):
        self.escrever(self.first_name_check_out, first_name)
        self.escrever(self.last_name_check_out, last_name)
        self.escrever(self.postal_code_check_out, zip_code)
        self.clicar(self.botao_continue_check_out)

    def finalizar_compra(self):
        self.clicar(self.botao_finish)
    
    def verificar_texto_error(self, texto_esperado):
        elemento = self.esperar_elemento_aparecer(self.check_out_message)
        texto_encontrado = elemento.text.strip()
        assert texto_encontrado == texto_esperado, (f"O texto encontrado foi '{texto_encontrado}', "f"mas era esperado o texto '{texto_esperado}'.")