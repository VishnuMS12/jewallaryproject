from django.db import models
class Jewelcate_Db(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name= models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Cat_img=models.ImageField(upload_to="Cat_img",null=True, blank=True)
class ornaments_Db(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name= models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Weight = models.CharField(max_length=100, null=True, blank=True)
    Item_gross_weight = models.CharField(max_length=100, null=True, blank=True)
    Item_net_weight = models.CharField(max_length=100, null=True, blank=True)
    Chain_length = models.CharField(max_length=100, null=True, blank=True)
    Diameter = models.CharField(max_length=100, null=True, blank=True)
    Ornaments_img1 = models.ImageField(upload_to="Orn_img", null=True, blank=True)
    Ornaments_img2 = models.ImageField(upload_to="Orn_img2", null=True, blank=True)
# Create your models here.
