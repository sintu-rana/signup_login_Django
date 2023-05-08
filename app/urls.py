from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='main.html'),
    path('register',views.register,name='register'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('task/',views.create_newuser,name='task'),
    # path('task-login/',views.task-login,name='task-login'),
    path('todolist',views.userlist,name='todolist'),
    path('todoedit<id>',views.useredit,name='todoedit'),
    path('tododelete<eid>',views.userdelete,name='tododelete'),
    path('todoadd',views.useradd,name='todoadd'),
     path('todoassign',views.userassign,name='todoassign'),
    path('task-login/',views.login2,name='task-login'),
    path('logout2/',views.logout2,name='logout2'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),


]

'''

  
'''       