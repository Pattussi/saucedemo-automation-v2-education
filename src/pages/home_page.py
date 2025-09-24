from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import conftest


class HomePage(BasePage): 
        
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//div[@class='product_label']") 
        self.intem_inventario = (By.XPATH,"//div[@class='inventory_item_name' and text()='{}']")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='ADD TO CART']")
        self.icone_carriho = (By.XPATH, "//*[@class='shopping_cart_container']")
       
    
    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.intem_inventario[0], self.intem_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carriho)