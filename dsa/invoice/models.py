from django.db import models

# Create your models here.
class Customer(models.Model):
    # id will be create automatically -> self.pk to access it
    customer_type = models.CharField(max_length=12)
    sirname = models.CharField(max_length=10)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    companyname = models.CharField(max_length=30,default="Google")
    displayname = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    mobilenumber = models.IntegerField()
    customerwebsite = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.firstname + self.lastname


class Products(models.Model):
    # id will be create automatically -> self.pk to access it 
    product_name = models.CharField(max_length=12)
    number_of_product = models.IntegerField()
    selling_price = models.IntegerField()
    product_desc = models.CharField(max_length=12)




    

