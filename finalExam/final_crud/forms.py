from django import forms
from final_crud.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['sid','name','email','password']