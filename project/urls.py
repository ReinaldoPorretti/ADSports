from django import contrib
from django.contrib import admin, auth
from django.urls import path, include
from adsports.views import home,camisasmasculino,shortsmasculino,tenismasculino,chuteirasmasculino,camisasfeminino,shortsfeminino,tenisfeminino,chuteirasfeminino,futebol,futebolamericano,basquete,volei,lancamentos,ofertas,produto,carrinho,perfil,funcao_login,funcao_logout,cadastrousuario,listaprodutos,cadastroproduto,createproduto,editarproduto,updateproduto,deleteproduto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('camisasmasculino/', camisasmasculino, name='camisasmasculino'),
    path('shortsmasculino/', shortsmasculino, name='shortsmasculino'),
    path('tenismasculino/', tenismasculino, name='tenismasculino'),
    path('chuteirasmasculino/', chuteirasmasculino, name='chuteirasmasculino'),
    path('camisasfeminino/', camisasfeminino, name='camisasfeminino'),
    path('shortsfeminino/', shortsfeminino, name='shortsfeminino'),
    path('tenisfeminino/', tenisfeminino, name='tenisfeminino'),
    path('chuteirasfeminino/', chuteirasfeminino, name='chuteirasfeminino'),
    path('futebol/', futebol, name='futebol'),
    path('futebolamericano/', futebolamericano, name='futebolamericano'),
    path('basquete/', basquete, name='basquete'),
    path('volei/', volei, name='volei'),
    path('lancamentos/', lancamentos, name='lancamentos'),
    path('ofertas/', ofertas, name='ofertas'),
    path('perfil/', perfil, name='perfil'),
    path('produto/<int:pk>/', produto, name='produto'),
    path('carrinho/', carrinho, name='carrinho'),
    path('login/', funcao_login, name='login'),
    path('logoutusuario/', funcao_logout, name='logoutusuario'),
    path('cadastrousuario/', cadastrousuario, name='cadastrousuario'),
    path('listaprodutos/', listaprodutos, name='listaprodutos'),
    path('cadastroproduto/', cadastroproduto, name='cadastroproduto'),
    path('createproduto/', createproduto, name='createproduto'),
    path('editarproduto/<int:pk>/', editarproduto, name='editarproduto'),
    path('updateproduto/<int:pk>/', updateproduto, name='updateproduto'),
    path('deleteproduto/<int:pk>/', deleteproduto, name='deleteproduto'),

] 


