from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")

        # Opção que mais aparece funcionando em projetos reais do saucedemo
        # Em HomePage.__init__ e CarrinhoPage.__init__
        self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name ' and normalize-space(.)='{}']")

        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)


    def adicionar_ao_carrinho(self, nome_item: str):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))

        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)