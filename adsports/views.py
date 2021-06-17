from django.shortcuts import render , redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from adsports.forms import ProdutoForm,CarrinhoForm
from adsports.models import Produtos, Carrinho

# Create your views here.

def home(request):
    return render(request,'index.html')

def camisasmasculino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='CamisasMasculinas')
    return render(request,'camisasmasculino.html',data)

def shortsmasculino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='ShortsMasculinos')
    return render(request,'shortsmasculino.html',data)

def tenismasculino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='TenisMasculinos')
    return render(request,'tenismasculino.html',data)

def chuteirasmasculino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='ChuteirasMasculinas')
    return render(request,'chuteirasmasculino.html',data)

def camisasfeminino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='CamisasFemininas')
    return render(request,'camisasfeminino.html',data)

def shortsfeminino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='ShortsFemininos')
    return render(request,'shortsfeminino.html',data)

def tenisfeminino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='TenisFemininos')
    return render(request,'tenisfeminino.html',data)

def chuteirasfeminino(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='ChuteirasFemininas')
    return render(request,'chuteirasfeminino.html',data)

def futebol(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='Futebol')
    return render(request,'futebol.html',data)

def futebolamericano(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='FutebolAmericano')
    return render(request,'futebolamericano.html',data)

def basquete(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='Basquete')
    return render(request,'basquete.html',data)

def volei(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='Volei')
    return render(request,'volei.html',data)

def lancamentos(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='Lançamentos')
    return render(request,'lancamentos.html',data)

def ofertas(request):
    data={}
    data['db'] = Produtos.objects.filter(categoria='Ofertas')
    return render(request,'ofertas.html',data)

def perfil(request):
    return render (request, 'perfil.html')


def produto(request,pk):
    data={}
    data['db'] = Produtos.objects.get(pk=pk)
    return render (request, 'produto.html', data)

def carrinho(request):
    return render(request,'carrinho.html',)

def funcao_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        authUser = authenticate(
            username = username,
            password = password,
        )
        if username == 'admin' and password == '123':
            login(request,authUser)
            return redirect ('/listaprodutos')
        elif authUser is not None:
            login(request,authUser)
            return redirect ('/')
        else:
            messages.error(request,'Dados inválidos!')
    return render(request,'registration/login.html')

def funcao_logout(request):
    logout(request)
    return redirect ('/')


def cadastrousuario(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname =  request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        createNewuser = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            username = username,
            email = email,
            password = password, 
        )
        createNewuser.save()
        return redirect ('/login')
    return render(request,'cadastro.html')

@login_required(login_url="/login/")
def listaprodutos(request):
    if User.is_staff:
        data={}
        data['db'] = Produtos.objects.all()
        return render(request,'listaprodutos.html',data)
    else:
        return redirect ('home')

def cadastroproduto(request):
    data={}
    data['formProduto'] = ProdutoForm()
    return render(request,'cadastroproduto.html',data)
    
def createproduto(request):
    formProduto = ProdutoForm(request.POST or None)
    if formProduto.is_valid():
        formProduto.save()
        return redirect('listaprodutos')

def editarproduto(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['formProduto'] = ProdutoForm(instance= data['db'])
    return render(request, 'editarproduto.html', data)

def updateproduto(request, pk):
    data= {}
    data['db'] = Produtos.objects.get(pk = pk)
    formProduto = ProdutoForm(request.POST or None , instance = data['db'])
    if formProduto.is_valid():
        formProduto.save()
        return redirect('listaprodutos')

        
def deleteproduto(request, pk):
    db = Produtos.objects.get(pk = pk)
    db.delete()
    return redirect('listaprodutos')