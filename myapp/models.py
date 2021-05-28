from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	image=models.ImageField(upload_to="user_image/",default="",blank="True",null="True")
	usertype=models.CharField(max_length=100,default="user")
	status=models.CharField(max_length=100,default="inactive")

	def __str__(self):
		return self.fname


class Product(models.Model):
	CHOICE=(
			('birthday','birthday'),
			('baby shower','baby shower'),
			('well come baby','well come baby'),
			('anniversary','anniversary'),
			('haldi','haldi'),
			('ring ceremony','ring ceremony'),
			('grand opening','grand opening'),
			('mehndi','mehndi')
		)

	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_category=models.CharField(max_length=100,choices=CHOICE)
	product_price=models.CharField(max_length=100)
	product_dec=models.TextField()
	product_image=models.ImageField(upload_to="ProductImage/")

	def __str__(self):
		return self.product_model


class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_category


