from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

JOB_CITY_CHOICE = [
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Nagpur', 'Nagpur'),
    ('Mumbai', 'Mumbai'),
    ('Hyderabad', 'Hyderabad'),
    ('Banglore', 'Banglore')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields="__all__"
        labels={'name': 'Full Name', 'dob': 'Date of Birth', 'pin': 'Pin Code', 'mobile': 'Mobile No.',
                    'email': 'Email ID', 'profile_image': 'Profile Image', 'my_resume': 'Document'}
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob':  forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
