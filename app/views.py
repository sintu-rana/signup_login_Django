from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.urls import reverse #####
from django.contrib.auth.decorators import login_required
# from .decorator import check_authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate as loginUser 
from .forms import *
from .models import *




# Create your views here.
# @login_required(login_url='login')
# def index(request):
#     return render(request,'index.html')


@login_required(login_url='login')
def index(request):
    form = TODOForm(request.POST)
    if form.is_valid():
        user = request.user
        print(form.cleaned_data)
        todo = form.save(commit=False)
        todo.user = user
        todo.save()
        messages.success(request, 'Todo Task is Uploaded successfully')
        print(todo)
        return redirect("/")
    else: 
        return render(request , 'index.html' , context={'form' : form})

'''
make a api with Admin<only access using that admin can create roles --> Manager/Employee

inputs --> email, username/f-name/l-name, role

extra --> password should be auto generated from backend side

compulsory-->admin ke time pe admin hi access honi chahiye


'''
# @staff_member_required
@login_required(login_url='login')
def register(request):
    # if request.user.is_superuser:
    if request.method == 'GET':
        user = CustomUser.objects.get(email=request.user)
        if user.role == 'ADMIN':
            return render(request,'register.html')
        else:
            messages.warning(request,"only admin can add role")
            return redirect('login')
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        role = request.POST.get('role')
        role = "MANAGER"
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'email is already exists')
            return redirect('register')
        # elif User.objects.filter(username=username).exits():
        #     messages.warning(request,'User Name is already exists')
        #     return redirect('register')
        else:
            try:
                user = CustomUser(email=email,password=password,first_name=firstname,
                last_name=lastname,username=username,role=role)
                user.set_password(password)
                user.save()
            except:
                messages.warning(request,"username is already registered")
                return redirect('register')
                
            subject = 'About Registration'
            message = f'Hi ,You has been registered successfully on website.'
            email_from = 'sinturana250@gmail.com'
            rec_list = [email,]
            response = send_mail(
                subject,
                message,
                email_from,
                rec_list,
                fail_silently=False
            )
            print("UYFRUYYUBTYUTBYUTUYBGUN", response)
            messages.success(request, 'User has been sucessfully registered')
            return redirect('/')
    return redirect(reverse('main.html'))
    


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('main.html'))
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid Credentials')
            # return redirect('login')
        return redirect(reverse('main.html'))
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


# def paper(request):
#     return render(request,'hello.html')


def create_newuser(request):
    if request.user.is_authenticated:
        return redirect(reverse('task.html'))
    if request.method=='POST':
        email = request.POST.get('email')
        my_password = CustomUser.objects.make_random_password()
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        role = request.POST.get('role')
        user = CustomUser(email=email,my_password=CustomUser.objects.make_random_password,first_name=firstname,
        last_name=lastname,
        username=username,
        role=role)
        user.save()
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'email is already exists')
            return redirect('task')
    return render(request,'task.html')

# def login2(request):
#     return render(request,'task-login.html')



# def userlist(request):
#     return render(request,'todolist.html')

@login_required(login_url='login')
def userlist(request):
    records=TODO.objects.all()
    mydict={'records':records}
    return render(request,'todolist.html',context=mydict)



def useredit(request,id=None):
    one_rec=TODO.objects.get(pk=id)
    form=TODOForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('todolist')
    mydict= {'form':form}
    return render(request,'todoedit.html',context=mydict)


# def useredit(request):
#     return render(request,'todoedit.html')


def userdelete(request,eid=None):
    one_rec = TODO.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('todolist')
    return render(request,'tododelete.html')




@login_required(login_url='login')
def userassign(request):
    form = ManagerForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        manager = form.save(commit=False)
        manager.CustomerUser = manager
        manager.save()
        return redirect("main.html")
    else: 
        return render(request , 'todoassign.html' , context={'form' : form})