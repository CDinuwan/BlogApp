from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    form=UserCreationForm()
    return render(request,'accounts/signup.html',{'from':form})
