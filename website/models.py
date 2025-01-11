from django.db import models



class Customer(models.Model):
	name = models.CharField(max_length=100,null=True)
	phone = models.CharField(max_length=20,blank=True)
	email = models.CharField(max_length=30,blank=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100,null=True)
	price = models.CharField(max_length=20)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	address = models.CharField(max_length=200)
	parent = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return "Order of "+self.parent.name  

class Images(models.Model):
	image = models.ImageField(null=True,blank=True,upload_to="pics/")
	




