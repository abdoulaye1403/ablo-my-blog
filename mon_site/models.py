from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
	nom=models.CharField(max_length=120) 
	def  __str__(self):
		return self.nom
	


class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	title = models.CharField(max_length=50)
	detail = models.TextField()
	image = models.ImageField()
	creer_le = models.DateTimeField(auto_now_add=True)
	modifier_le = models.DateTimeField(auto_now=True) 
	categorie= models.ForeignKey(Categorie,on_delete=models.CASCADE)



	def  __str__(self):
		return self.title
 
 