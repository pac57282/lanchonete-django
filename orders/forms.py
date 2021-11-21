from django import forms 
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            'first_name':'Nome', 'last_name':'Sobrenome', 'email':'E-Mail', 'address':'Logradouro', 'postal_code':'CEP', 'city':'Cidade'
        }
        