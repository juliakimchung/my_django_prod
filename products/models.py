from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    """
    The customers table integrates the Django User model and maintains relevant information for a customer
    
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Customers"

        def __str__(self):
            return '{}'.format(self.user.username)






class ProductType(models.Model):

    """ 
    This class is to represent a category of products on Bangazon
    Extension of models.Model
    Variables:
        label: the Product type's name
    """
    label = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.label

    """
    Method to create a string representing a Product Category of
    Bangazon API
    """

    class Meta:

        ordering=('label',)

class Product(models.Model):
    """
    Class to represent a product for sale on Bangazon
    tied to a
    particular User(customer) of bangazon API
    Extension of models.Model
    Variables:
        created: the current local date and time of creation
        name: the product's name
        
        customer: the foreign key of the user, related_name is for the PaymentMethod model: related_name should be lowercase, pluralized model name
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=300, default='')
    quantity = models.IntegerField()
    product_type =models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=True, unique=True)
    customer =models.ForeignKey(Customer,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        """
        Method to create a string representing a Product sold/bought by a particular User(customer)
     
        """

    class Meta:
        ordering =('name', )


class PaymentType(models.Model):
    """
    This is a class to represent a payment method to a user of  bangazon api
    Variables:
        created: the current local date and time of creation
        name: the payment method's name
        account_number: the payment method's unique identifier
        user: the foreign key of the user, related_name is for the PaymentMethod model: related_name should be lowercase, pluralized model name
    """

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default="")
    account_number = models.CharField(max_length=100, blank=True, default="")
    cvv_number = models.CharField(max_length=4, blank=True, default="")
    expiration_date = models.DateField()
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Payment Method
        table of Bangazon API
        """
        ordering = ('name', )



class Orders(models.Model):
    """
    Class to create a table representing an Order, tied to a
    particular User(customer) of bangazon API
    Extension of models.Model
    Variables:
        active: A boolean denoting whether the order is being processed
        created: the current local date and time of creation
        payment_method_id: the foreign key of the user's payment method, only
            needed when the order is "active", related_name is for the Order model: related_name should be lowercase, pluralized model name
        user: the foreign key of the User(customer)related_name is for the Order model: related_name should be lowercase, pluralized model name
    """
    active = models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True)
    customer =models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    product =models.ManyToManyField(Product, related_name='orders')
    payment_type = models.ForeignKey(PaymentType,  related_name='orders',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    """
        Method to create a string representing a Order of a particular User
        (customer) of Bangazon API
    """

    class Meta:
        ordering=('customer', )
