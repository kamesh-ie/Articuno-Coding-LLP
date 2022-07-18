from django.shortcuts import render,redirect
from .forms import CreateUserForm
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
            print('error')
    return render(request,'signin.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('error',form.error_messages,form.errors)
    
    context = {
        'form':form,
    }
    

    return render(request,'signup.html',context)

def signout(request):
    logout(request)
    return redirect('/')



@login_required(login_url='signin')
def index(request):

    return render(request,'index.html')