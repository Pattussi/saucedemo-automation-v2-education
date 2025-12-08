import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# A LoginPage representa a tela de login do sistema.
# Centralizamos aqui os elementos e ações referentes ao login.

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # Localizadores dos elementos da tela
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_login = (By.XPATH, "//h3[@data-test='error']")

    def fazer_login(self, usuario, senha): 
        # --- Versão com POM (boa prática) --- #
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

        # --- Versão sem POM (deixada comentada como didática) --- #
        # self.driver.find_element(*self.username_field).send_keys(usuario)
        # self.driver.find_element(*self.password_field).send_keys(senha)
        # self.driver.find_element(*self.login_button).click()

    def verificar_mensagem_erro_login_existe(self):
        # Valida se a mensagem de erro de login aparece na tela
        self.verificar_se_elemento_existe(self.error_login)
    
    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        # Valida o texto da mensagem de erro
        texto_encontrado = self.pegar_texto_elemento(self.error_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'."

    