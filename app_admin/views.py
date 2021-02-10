from django.shortcuts import render 
from mon_site.models import Article

# Create your views here.
def dashbord(request):
	return render(request, "db.html")

def user_articles(request):
	list_articles = Article.objects.filter(user=request.user)
	return render(request, "my-articles.html", {"list_articles":list_articles})
