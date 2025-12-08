import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# A FinishPage representa a tela final da compra,
# onde aparece a mensagem de confirmação.

class FinishPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # Localizador da mensagem de confirmação
        self.finish_message = (By.XPATH,"//h2[@class='complete-header' and text()='Thank you for your order!']")

    def verificar_texto_compra_finalizada(self, texto_esperado):
        # Valida se a mensagem de sucesso corresponde ao esperado
        elemento = self.esperar_elemento_aparecer(self.finish_message)
        texto_encontrado = elemento.text.strip()
        assert texto_encontrado == texto_esperado, (f"O texto encontrado foi '{texto_encontrado}', "f"mas era esperado o texto '{texto_esperado}'.")
    