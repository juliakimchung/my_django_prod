from django.shortcuts import render, get_object_or_404
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
class CreateProduct(TemplateView):
    template_name = 'products/create_product.html'

    def post(self, request):
        data = request.POST
        product_type = ProductType.objects.get_or_create(label=data['label'])
        Product.objects.create(
            name=data['name'],
            price=data['price'],
            description=data['description'],
            quantity=data['quantity'],
            product_type = product_type[0],
            customer= request.user
            
            )
        return HttpResponseRedirect(redirect_to='/products/list')


def product_type(request):
    product_type_list = ProductType.objects.order_by('label')[:20]
    context = {'product_type_list': product_type_list,}
    return render(request, 'products/product_type_list.html', context)


class  CreateProductType(TemplateView):

    template_name = 'products/create_product_type.html'

    def post(self, request):
        data = request.POST
        ProductType.objects.create(
            label=data['label'])

        return HttpResponseRedirect(redirect_to='/products/product_type_list')

class ProductDetail(TemplateView):
    template_name = 'products/product_detail.html'

    def post_detail(request, pk):
        instance = Product.objects.get_object_or_404(Product, id=pk)
        context = {
        "title":instance.title,
        'instance': instance
        }

        retrun(request, 'product_detail.html', context)
class Register(TemplateView):
    template_name = 'products/register.html'

    def post(self,request):
        data = request.POST
        current_user=User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        Customer.objects.create(
            user = current_user,
            address=data['address'],
            city=data['city'],
            state=data['state'],
            zip_code=data['zip_code'],
        )

        return HttpResponseRedirect(redirect_to='/products/login')

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

