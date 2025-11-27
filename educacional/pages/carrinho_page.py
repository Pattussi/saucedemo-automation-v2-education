import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# A CarrinhoPage representa a tela do carrinho de compras.

class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver  
        # Localizadores
        self.item_inventario = (By.XPATH,"//div[@class='inventory_item_name' and text()='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")
        self.botao_check_out = (By.ID, "checkout")
        self.botao_remover = (By.ID, "remove-sauce-labs-backpack")
    
    def verificar_produto_carrinho_existe(self, nome_item):
        # Verifica se um produto específico está no carrinho
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)
    
    def clicar_continuar_comprando(self):
        # Retorna à tela inicial para continuar adicionando produtos
        self.clicar(self.botao_continuar_comprando)
    
    def clicar_botao_check_out(self):
        # Avança para a etapa de checkout
        self.clicar(self.botao_check_out)
    
    def remover_item_do_carrinho(self, nome_item):
        # Remove um item específico do carrinho
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(self.botao_remover)

    def verificar_produto_nao_existe(self, nome_item):
        # Verifica se um produto específico não está mais no carrinho
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_elemento_não_existe(item)

    def obter_quantidade_itens(self):
        # Retorna a quantidade de itens atualmente no carrinho
        itens = self.encontrar_elementos((By.CLASS_NAME, "inventory_item_name"))
        return len(itens)
    

