from django.conf.urls import url
from . import views

app_name = 'products_app'
urlpatterns = [
url(r'^list$', views.home, name="home"),
url(r'^create/$', views.CreateProduct.as_view(), name="create"),
url(r'^product_type_list/$', views.product_type, name='product_type_list'),
url(r'^create_product_type/$', views.CreateProductType.as_view(), name='create_product_type'),
url(r'^(?P<pk>\d/+)/$',views.ProductDetail.as_view(), name='product_detail'),
url(r'^register/$', views.Register.as_view(), name="register"),
url(r'^login/$', views.Login.as_view(), name='login'),
url(r'^logout/$', views.logout_user, name="logout"),
]