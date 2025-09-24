import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FinishPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver  
        self.finish_message = (By.XPATH,"//h2[@class='complete-header' and text()='THANK YOU FOR YOUR ORDER']")

    def verificar_texto_compra_finalizada(self, texto_esperado):
        elemento = self.esperar_elemento_aparecer(self.finish_message)
        texto_encontrado = elemento.text.strip()
        assert texto_encontrado == texto_esperado, (f"O texto encontrado foi '{texto_encontrado}', "f"mas era esperado o texto '{texto_esperado}'.")
    