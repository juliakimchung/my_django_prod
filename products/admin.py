from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(PaymentType)
admin.site.register(Orders)
