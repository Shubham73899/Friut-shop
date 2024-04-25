from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    frist_name = models.CharField(max_length = 50)   
    last_name = models.CharField(max_length = 50)  
    phone = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    password= models.CharField(max_length = 50)

    def __str__(self):
        return self.frist_name,self.last_name
    
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='uploads/')
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    adress=models.CharField(max_length=200,null = False, blank = True)
    phone=models.CharField(max_length=20)
    date=models.DateField(default = datetime.datetime.today)
    status=models.BinaryField(default= False)

    def __str__(self):
        return self.Product