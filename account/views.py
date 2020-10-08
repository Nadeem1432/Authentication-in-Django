from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User  # sign me user create ke liye module
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request,"account/home.html")


def login(request):
    if request.method=='POST':
        user=auth.authenticate(username = request.POST['username'] , password = request.POST['password'])
        if user is  not None:
            auth.login(request,user)
            return render(request,'account/login_success.html')
        else:
            return render(request,"account/login.html",{'error':'username or password is incorrect !!! '})
    else:
        return render(request,"account/login.html")


def signup(request):
    if request.method == 'POST': #signup ke button par click krdiya h
        if request.POST['password1'] == request.POST['password2']: #password confirm ke liye
            try:
                user = User.objects.get(username = request.POST['username']) #is name se allready account to nahi hai
                return render(request,"account/signup.html",{'error':'username is allready taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'] , password = request.POST['password1']) #yaha se user create hojyga
                auth.login(request,user) # yaha par automatic login hojyga
                return redirect('home') # or yaha ane par automatic hmara signup hokr homapage khul jayega

        else:
            return render(request,"account/signup.html",{'error':'password dosen\'t matched....please enter the same password in both feilds'})

    else:
        return render(request,"account/signup.html")
