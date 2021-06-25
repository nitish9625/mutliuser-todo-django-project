from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import TodoForm
from.models import Todo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def index(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        forms = TodoForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            todo = forms.save(commit=False)
            todo.user = user
            todo.save()
    if request.user.is_authenticated:
        user = request.user
        todos = Todo.objects.filter(user=user).order_by('priority')
    return render(request, "index.html", {'todos':todos, 'forms':forms})

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

def change_status(request, id, status):
    todo = Todo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('/')

def edit(request, id):  
    todo = Todo.objects.get(id=id) 
    return render(request,'update.html', {'todo':todo})

def update(request, id):
    # if request.user.is_authenticated:
    #     user = request.user
    #     print(user)
    todo = Todo.objects.get(id=id)
    forms = TodoForm(request.POST, instance=todo)
    if forms.is_valid():
        print(forms.cleaned_data)
    return render(request,"update.html", {'todo':todo}) 

def register_page(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username name is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password = password1)
                user.save()
                print('user create')
        else:
            messages.info(request, 'password is not matching')
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")

def login_page(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid username or password")
            return redirect("login")
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")