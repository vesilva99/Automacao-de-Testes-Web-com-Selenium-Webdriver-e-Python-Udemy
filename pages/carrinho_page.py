import conftest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class CarrinhoPage(HomePage):

    def __init__(self):
        self.driver = conftest.driver
        # Em HomePage.__init__ e CarrinhoPage.__init__
        self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name' and normalize-space(.)='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")

    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)
