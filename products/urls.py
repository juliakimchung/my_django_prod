from django.conf.urls import url
from . import views

app_name = 'products_app'
urlpatterns = [
url(r'^list$', views.home, name="home"),
url(r'^product/$', views.create_product, name="product"),
url(r'^create/$', views.template_to_create, name="create"),
url(r'^product_type/$', views.create_product_type, name='product_type'),
url(r'^product_type_list/$', views.product_type, name='product_type_list'),
url(r'^create_product_type/$', views.template_to_create_product_type, name='create_product_type'),
url(r'^register/$', views.Register.as_view(), name="register"),
url(r'^login/$', views.login_user, name='login'),
url(r'^logout/$', views.logout_user, name="logout"),
]