from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def home(request):
    product_list = Product.objects.order_by('created')[:20]
    context = {'product_list': product_list,}
    return render(request, 'products/product_list.html', context)
def create_product(request):
    data = request.POST
    product_type = ProductType.objects.get_or_create(label=data['label'])
    Product.objects.create(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        quantity=data['quantity'],
        product_type =product_type[0],
        customer=request.user)
    return HttpResponseRedirect(redirect_to='/products/list')

def template_to_create(request):
    return render(request, 'products/create_product.html')

def product_type(request):
    product_type_list = ProductType.objects.order_by("label")[:20]
    context = {'product_type_list': product_type_list,}
    return render(request, 'products/product_type_list.html', context)


def create_product_type(request):
    data = request.POST
    ProductType.objects.create(
        label=data['label'])

    return HttpResponseRedirect(redirect_to='/products/product_type_list')


def template_to_create_product_type(request):
    return render(request, 'products/create_product_type.html')

class Register(TemplateView):
    template_name = 'products/register.html'
    current_customer = User.customer
    def post(self,request):
        data = request.POST
        current_customer.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            )
        return login_user(request)
class Login(TemplateView):
    template_name = 'products/login.html'

    def post(self, request):

        data=request.POST
        username=data['username']
        password=data['password']
        user=authenticate(
            username=username,
            password=password)
        if user is not None:
            login(request=request, user=user)
        else:
            return HttpResponseRedirect(redirect_to='/')
        return HttpResponseRedirect(redirect_to='/products/list')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')

