from django import forms
from .models import ClassStream, Student

class StreamForm(forms.ModelForm):
    class Meta:
        model = ClassStream
        fields = ["stream_name"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "class_stream"]
