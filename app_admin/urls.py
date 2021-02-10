from django.urls import path
from .views import *
urlpatterns = [
    path('', dashbord, name="dashbord"),
    path('my-articles',user_articles,name="my-articles"),
    

]
  