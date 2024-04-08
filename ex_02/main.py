from pedido import Pedido
from item_pedido import ItemPedido
from produto import Produto

iphone11 = Produto(1, 2000.00, "Iphone 11")
iphone12  = Produto(2, 3000.00, "Iphone 12")
iphone13 = Produto(3, 4000.00, "Iphone 13")
iphone15  = Produto(4, 14000.00, "IPhone 15")

p1 = Pedido()
item = ItemPedido(iphone11,2)
p1.adicionar_item(item)
item = ItemPedido(iphone12,1)
p1.adicionar_item(item)
item = ItemPedido(iphone13,3)
p1.adicionar_item(item)
print("Valor total do pedido 1(iphone 11,12,13) = ", p1.obter_total())

p2 = Pedido()
item = ItemPedido(iphone15, 1)
p2.adicionar_item(item)

print("Valor total do pedido 2(iphone 15) = ", p2.obter_total())

# for x in p2.itens_pedido:
#     print(x.produto.descricao)
    