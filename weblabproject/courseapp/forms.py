from django import forms
# from . import models
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        # model = models.Course
        model = Course
        fields = "__all__"


# <<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#for better look:
        widgets = {
            "course_id":forms.TextInput(attrs={'class':'form-control'}),
            "course_name":forms.TextInput(attrs={'class':'form-control'}),
            "course_credit":forms.TextInput(attrs={'class':'form-control'}),
            "ct_full_marks":forms.TextInput(attrs={'class':'form-control'}),
            "att_full_marks":forms.TextInput(attrs={'class':'form-control'}),
            "final_full_marks":forms.TextInput(attrs={'class':'form-control'}),
        }