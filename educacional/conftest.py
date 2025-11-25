import pytest
from selenium import webdriver

# Este arquivo é utilizado pelo pytest para configurar os testes.
# Aqui usamos o conceito de "fixture", que prepara o ambiente antes dos testes
# (setup) e depois limpa o ambiente (teardown).
# Isso garante que cada teste seja executado de forma independente.

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # --- Setup --- #
    # Inicia o navegador antes de cada teste
    global driver 
    driver = webdriver.Chrome()
    driver.implicitly_wait(3) # espera implícita de 3s para todos os elementos
    driver.maximize_window()
    driver.get("https://www.saucedemo.com") # site alvo

    # "yield" entrega o controle para o teste rodar neste ponto
    yield

    # --- Teardown --- #
    # Após o teste, fecha o navegador
    driver.quit()
