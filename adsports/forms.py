from django.db.models import fields
from django.forms import ModelForm, widgets
from adsports.models import Produtos, Carrinho

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome','preco','descricao','estoque','categoria']

class CarrinhoForm(ModelForm):
    class Meta:
        model = Carrinho
        fields = ['nome_usuario','nome_produto','preco', 'quantidade', 'total']