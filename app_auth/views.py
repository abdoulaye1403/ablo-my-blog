from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import LoginForm

def login_blog(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user=authenticate(username=username,password=pwd)
            if user is not None:

                return redirect('home')
            else: 
                messages.error(request,"authentification échouée")
                return render(request ,"login.html", {'form':form})   
        else:
            for field in form:
                field.field.widget.attrs['class'] = (field.field.widget.attrs.get('class') or '') + " is-invalid"
            return render(request ,'login.html', {'form':form}) 
    else:   
       form = LoginForm()
       return render(request,'login.html',{'form':form}) 

   
   