from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.urls import reverse #####
from django.contrib.auth.decorators import login_required
# from .decorator import check_authenticate


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

'''
make a api with Admin<only access using that admin can create roles --> Manager/Employee

inputs --> email, username/f-name/l-name, role

extra --> password should be auto generated from backend side

compulsory-->admin ke time pe admin hi access honi chahiye


'''
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('main.html'))
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        role = request.POST.get('role')
        
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
        # return redirect(reverse('main.html'))
    return render(request,'register.html')


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

def task(request):
    return render(request, 'task.html')