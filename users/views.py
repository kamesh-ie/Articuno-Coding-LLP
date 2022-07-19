from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,'signin.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Succsfully registered"+name)
            return redirect('/')
        else:
            print('error',form.error_messages,form.errors)
    
    context = {
        'form_errors':form.errors,
    }
    

    return render(request,'signup.html',context)

def signout(request):
    logout(request)
    return redirect('/')



@login_required(login_url='signin')
def index(request):

    return render(request,'index.html')


def modals(request):
    return render(request,'modals.html')