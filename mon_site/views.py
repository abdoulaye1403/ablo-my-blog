from django.shortcuts import render
from .models import Article
# Create your views here.
def home(request):
	list_article=Article.objects.all()
	context={"list_article":list_article}
	return render(request, "index.html",context)

def detail(request,id_article):
	   article=Article.objects.get(id=id_article)
	   categorie=article.categorie 
	   article_en_relation=Article.objects.filter(categorie=categorie)[:6]
	   context={"article":article,"aer":article_en_relation}
	   return render(request,'detail.html',context)  

def recherche(request): 
	   query=request.GET["article"] 
	   article=Article.objects.filter(title__icontains=query)
	   return render(request,'recherche.html',{"article":article})  