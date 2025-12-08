from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)


    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)


    def escrever(self, locator, text):
        elemento = self._esperar_visibilidade(locator)
        elemento.clear()
        elemento.send_keys(text)


    def clicar(self, locator):
        elemento = self._esperar_visibilidade(locator)
        elemento.click()


    def verificar_se_elemento_existe(self, locator):
        assert self._esperar_visibilidade(locator), \
            f"Elemento {locator} não está visível na tela."


    def pegar_texto_elemento(self, locator):
        elemento = self._esperar_visibilidade(locator)
        return elemento.text


    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )


    def _esperar_visibilidade(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )


    def verificar_elemento_existe(self, locator):
        assert self.esperar_elemento_aparecer(locator), \
            f"Elemento {locator} não foi encontrado"


    def verificar_elemento_não_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, \
            f"Elemento {locator} foi encontrado, mas não deveria estar presente"