from django.shortcuts import render

def check_authenticate(myfunc):
    def inner(request):
        if request.user.is_authenticated:
            return render(request,'app/login.html')
        else:
            return myfunc(request)
    return inner