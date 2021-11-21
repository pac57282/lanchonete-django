from django import forms

PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):   #fomrulário para adicionar produtos no carrinho
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int)   #permite adicionar de 1 a 20 itens no carrinho e converte a entrada para int
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)   #informa a quantidade a ser somada a uma quantidade existente, ou a quantidade existente deve ser sobrescrita

