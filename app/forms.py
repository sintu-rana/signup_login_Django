from django.forms import ModelForm

from app.models import TODO


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['task' , 'status' , 'priority']

# class ManagerForm(ModelForm):
#     class Meta:
#         model = Manager
#         fields = ['user' , 'employee']
        

       