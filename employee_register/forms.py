from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'Employee Code'
        }

     # this function is for the dropdown because by default
     # dropdown have some ------ lines but using this functionwe set the default 
     # value of function is select 
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        #if we want to remove the required field
        self.fields['emp_code'].required = False