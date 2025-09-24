from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import conftest

# A HomePage representa a tela inicial do sistema após o login.
# Aqui ficam os elementos e as ações relacionadas ao inventário de produtos.

class HomePage(BasePage): 
        
    def __init__(self):
        self.driver = conftest.driver
        # Localizadores dos elementos da página
        self.titulo_pagina = (By.XPATH, "//div[@class='product_label']") 
        self.intem_inventario = (By.XPATH,"//div[@class='inventory_item_name' and text()='{}']")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='ADD TO CART']")
        self.icone_carriho = (By.XPATH, "//*[@class='shopping_cart_container']")
       
    
    def verificar_login_com_sucesso(self):
        # Verifica se o login foi feito com sucesso, checando se o título aparece
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        # Localiza o item pelo nome e adiciona ao carrinho
        item = (self.intem_inventario[0], self.intem_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        # Clica no ícone do carrinho para abrir a tela do carrinho
        self.clicar(self.icone_carriho)
