from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from category.models import Categorie
from django.contrib import messages

from product.models import Product
from user.models import User
# Create your views here.
@login_required
def index(request):
    return render(request,'dashboard/index.html')

@login_required
def teller_view(request):
    categories=Categorie.objects.all()
    articles= Product.objects.all().order_by('libelle')
    context={
        'categories':categories,
        'articles':articles,
    }
    
    return render(request,'teller/index.html',context)
