from django.shortcuts import render

# Create your views here.
def signup_view(request):
    return render(request,'accounts/signup.html')
