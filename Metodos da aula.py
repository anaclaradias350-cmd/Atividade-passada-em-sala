class Produto:
    def __init__ (self, nome, categoria, preço, estoque):
        self.nome = nome
        self.categoria = categoria
        self.preço = preço
        self.estoque = estoque

    def exibir (self):
     print (f"Produto : (self.nome) ")
     print (f"Categoria : (self.categoria) ")
     print (f" Preço : (self.preço) ")
     print (f"Estoque : (self.estoque) ")

def valor_total (self):
   return self.preço * self.estoque

def aplicar_descontos(self, percentual):
   self.preço *= (1 - percentual / 100)
   print (f"Desconto aplicado! Novo preço: R$ (self.preço)")

def vender (self, quantidade):
   if quantidade > self.estoque:
      print ("Estoque insuficiente!")
   else:
    self.estoque -= quantidade
    print (f"Vendido {quantidade} x {self.nome}.Estoque restante: (self.estoque)")

def repor_estoque (self, quantidade):
   self.estoque += quantidade
   print (f"Novo estoque: {self.estoque}")
