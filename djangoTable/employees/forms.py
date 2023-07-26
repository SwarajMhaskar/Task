# myapp/forms.py
from django import forms
from .models import TableRow

class TableRowForm(forms.ModelForm):
    class Meta:
        model = TableRow
        fields = ['emp_id','name', 'email', 'department', 'job_title', 'date_of_joining', 'salary']
