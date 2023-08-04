from django.shortcuts import render
from .forms import UserForm
from .models import UserDetails
# Create your views here.


def user_auth(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'usermodule/login.html',{'message':'Account created sucessfully, Login now','form':form})
    
    else:
        form  = UserForm()
        return render(request,'usermodule/user_auth.html',{'form':form})
