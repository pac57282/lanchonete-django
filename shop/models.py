from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)   #nome da categoria
    slug = models.SlugField(max_length=200, unique=True)   #slug para criação de indice

    class Meta:
        ordering = ('name',)  
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):   #obter o URL de um objeto
        return reverse('shop:product_list_by_category', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)   #relacionamento (one-to-many) um para muitos - um produto pertence a uma categoria e uma categoria contém vários produtos
    name = models.CharField(max_length=200, db_index=True)   #nome do produto
    slug = models.SlugField(max_length=200, db_index=True)   #serve para compor URLs elegantes
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)   #imagem opcional para os produtos
    description = models.TextField(blank=True)   #descrição opcional para o produto
    price = models.DecimalField(max_digits=10, decimal_places=2)   #campo de preço
    available = models.BooleanField(default=True)   #campo booleano para informar se o produto esta disponível, será usado para ativar/desativar o produto nos catálogos
    created = models.DateTimeField(auto_now_add=True)   #armazena a data de criação
    updated = models.DateTimeField(auto_now=True)   #armazena quando o produto foi atualizado pela última vez
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):   #obter o URL de um objeto
        return reverse('shop:product_detail', args=[self.id, self.slug])
    