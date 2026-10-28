from django.db import models

class ContactDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email= models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class Registerdb(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password= models.CharField(max_length=100, null=True, blank=True)
    confirm_password = models.CharField(max_length=100, null=True, blank=True)
    Mobile_number = models.IntegerField(max_length=100, null=True, blank=True)
    Email_id = models.CharField(max_length=100, null=True, blank=True)

class CartDB(models.Model):
    user_name= models.CharField(max_length=100, null=True, blank=True)
    Product_name=models.CharField(max_length=100, null=True, blank=True)
    Quantity=models.IntegerField( null=True, blank=True)
    Price=models.IntegerField( null=True, blank=True)
    Total_price=models.IntegerField( null=True, blank=True)
    Prod_img=models.ImageField(upload_to="cartimg", null=True, blank=True)

class OrderDB(models.Model):
    First_name = models.CharField(max_length=100, null=True, blank=True)
    Last_name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    ZIP_Code = models.IntegerField(null=True, blank=True)



