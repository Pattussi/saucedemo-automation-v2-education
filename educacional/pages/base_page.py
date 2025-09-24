import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

# A classe BasePage é a classe "pai" de todas as páginas do sistema.
# Nela centralizamos métodos comuns como clicar, escrever em campos,
# pegar texto, validar existência de elementos, etc.
# Isso evita repetição de código em cada página específica.

class BasePage:
    def __init__(self):
        # O driver é compartilhado através do conftest
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        # Localiza UM elemento usando o locator (tupla By, valor)
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        # Localiza vários elementos (ex.: lista de produtos)
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        # Insere texto em um campo (ex.: login, senha, CEP)
        self.encontrar_elemento(locator).send_keys(text)
    
    def clicar(self, locator):
        # Clica em um botão, link ou qualquer elemento clicável
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        # Assegura que o elemento está visível na tela
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        # Espera o elemento aparecer e depois retorna seu texto
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text    
    
    def esperar_elemento_aparecer(self, locator, timeout=10):
        # Espera explícita até que o elemento esteja presente
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def verificar_elemento_existe(self, locator):
        # Verifica que o elemento realmente existe
        assert self.encontrar_elemento(locator), f"Elemento '{locator}' não existe, mas era esperado que existisse."

    def verificar_elemento_não_existe(self, locator):
        # Verifica que o elemento não está presente (importante em cenários negativos)
        assert len(self.encontrar_elementos(locator)) == 0 , f"Elemento '{locator}' existe, mas é esperado que não exista."

    def clique_duplo(self, locator):
        # Exemplo de ação avançada: clique duplo
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()
    
    def clique_botao_direiro(self, locator):
        # Exemplo de ação avançada: clique com botão direito
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()
    
    def pressionar_tecla(self, locator, key):
        # Simula pressionamento de teclas (ENTER, ESPAÇO, etc.)
        elem = self.encontrar_elemento(locator)
        if key == "ENTER":
            elem.send_keys(Keys.ENTER)
        elif key == "ESPACO":
            elem.send_keys(Keys.SPACE)
