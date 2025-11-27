from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import conftest

# A HomePage representa a tela inicial do sistema após o login.
# Aqui ficam os elementos e as ações relacionadas ao inventário de produtos.

class HomePage(BasePage): 
        
    def __init__(self):
        self.driver = conftest.driver
        # Localizadores dos elementos da página
        self.titulo_pagina = (By.XPATH, "//div[@class='app_logo']") 
        self.item_inventario = (By.XPATH,"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='{}']")
        self.botao_adicionar_carrinho = (By.ID, "add-to-cart")
        self.icone_carriho = (By.XPATH, "//*[@class='shopping_cart_container']")
        self.botao_menu = (By.ID, "react-burger-menu-btn")
        self.botao_logout = (By.ID, 'logout_sidebar_link')
        self.botao_filtro = (By.CLASS_NAME, "product_sort_container")
        self.opcao_high_to_low = (By.XPATH, "//option[@value='hilo']")
        self.locator_precos = (By.CLASS_NAME, "inventory_item_price")
        self.opcao_a_to_z = (By.XPATH, "//option[@value='az']")
       
    #//select[@class="product_sort_container"]
    def verificar_login_com_sucesso(self):
        # Verifica se o login foi feito com sucesso, checando se o título aparece
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        # Localiza o item pelo nome e adiciona ao carrinho
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        # Clica no ícone do carrinho para abrir a tela do carrinho
        self.clicar(self.icone_carriho)

    def fazer_logout(self):
        self.clicar(self.botao_menu)   # abre o menu lateral
        self.esperar_elemento_aparecer(self.botao_logout) # espera o botão de logout aparecer
        self.clicar(self.botao_logout) # clica no botão de logout

    def aplicar_filtro_decrescente(self):
        self.clicar(self.botao_filtro)
        self.clicar(self.opcao_high_to_low) # seleciona a opção "Price (high to low)"
        
    def obter_precos(self):
        elementos_precos = self.driver.find_elements(*self.locator_precos)    
        return [float(p.text.replace("$", "")) for p in elementos_precos] 
        # Extrai os preços e converte para float, removendo o símbolo "$"
    
    def precos_em_ordem_decrescente(self):
        valores = self.obter_precos()
        return valores == sorted(valores, reverse=True)
        # Verifica se os preços estão em ordem decrescente
    
    def aplicar_filtro_ascendente(self):
        self.clicar(self.botao_filtro)
        self.clicar(self.opcao_a_to_z) 
        # seleciona a opção "Name (A to Z)"
        
    def produtos_em_ordem_ascendente(self):
        nomes = [e.text for e in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        return nomes == sorted(nomes)
        # Verifica se os nomes dos produtos estão em ordem alfabética crescente


    
        