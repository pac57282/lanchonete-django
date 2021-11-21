from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):   #classe que iré gerenciar o carrinho de compras

    def __init__(self, request):
        #Inicializa o carrinho de compras
        self.session = request.session   #armazenando a sessão atual
        cart = self.session.get(settings.CART_SESSION_ID)   #tentar obter um carrinho da sessão atual
        if not cart:   #se não houver um carrinho, criamos um vazio
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add (self, product, quantity=1, override_quantity=False):   #o médoto add aceita o produtoa ser adicionado ou atualizado, a quantidade, onde seu valo default é 1, e o booleano ue informa se a quantidade deve ser sobrescrita ou somada a existente
        #Adiciona um produto no carrinho de compras ou atualiza a sua quantidade
        product_id = str(product.id)   #o id do produto serve como chave no dicionário, que representa o conteúdo do carrinho, o id foi convertido em string, pq o django utiliza json para serializar os dados de sessão
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price': str(product.price)}   #o preço do produto é convertido de decimal para string para que seja serializado
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()   #salva o carrinho na sessão

    def save(self): 
        #marca a sessão como "modificada" para garantir que ela seja salva
        self.session.modified = True

    def remove(self, product):
        #remove um produto do carrinho de compras e chama o método save para atualizar o carrinho de compras
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
 
    def __iter__(self):
        #itera pelo itens do carrinho de compras e obtém os produtos do banco de dados
        product_ids = self.cart.keys()
        #obtém os objetos referentes aos produtos e os adiciona no carrinho
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        #Contabiliza todos os itens que estão no carrinho de compras
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        #calcular o custo total dos itens do carrinho
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        #remove o carrinho da sessão
        del self.session[settings.CART_SESSION_ID]
        self.save()

        