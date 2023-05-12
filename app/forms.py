from django.forms import ModelForm

from app.models import TODO, Manager, Employee


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['task' , 'status' , 'priority', 'employee']

class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['user' , 'employee']
        

       