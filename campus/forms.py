from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import stu_details,job_poss
from django.forms.widgets import DateInput,CheckboxSelectMultiple
from django.http import request
from django.core.validators import RegexValidator




class Student_SignUpForm(UserCreationForm):
    branch_choices = (
        ('IT', 'Information_Technology'),
        ('Mech', 'Mech'),
        ('Civil', 'Civil'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('Chem', 'Chemical'),
        ('CSE', 'CSE'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'))

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name=forms.CharField(max_length=30, required=True,validators=[alphanumeric], help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Enter Name','autocomplete':'off'}))
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{10,10}$")
    phone_number = forms.RegexField(regex=r'^\+?1?\d{10,10}$',help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Enter Phone Number','autocomplete':'off'}))
    gender = forms.ChoiceField( choices=gender, required=True,help_text='*required')
    place = forms.CharField(max_length=30, validators=[alphanumeric],required=True,help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Where Do You Stay?','autocomplete':'off'}))
    branch = forms.ChoiceField( choices=branch_choices, required=True,help_text='*required')
    cgpa_Btech = forms.FloatField(max_value=10, min_value=1, required=True,help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Average CGPA','autocomplete':'off'}))
    class_10_percentage = forms.FloatField(max_value=100, min_value=0, required=True,help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'10th %','autocomplete':'off'}))
    class_12_percentage = forms.FloatField(max_value=100, min_value=0, required=True,help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'12th %','autocomplete':'off'}))
    certifications_count = forms.IntegerField(required=True,help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'How Many Certificates You Have?','autocomplete':'off'}))
    languages = forms.CharField(max_length=100, required=True, help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Enter Languages','autocomplete':'off'}))
    dob = forms.DateField(required=True, help_text='*format is YYYY-MM-DD',widget=forms.TextInput(attrs= {'placeholder':'Enter Your Birth Date','autocomplete':'off'}))
    sop = forms.CharField(max_length=500, help_text='*required', widget=forms.Textarea(attrs= {'placeholder':'Enter Statement Of Purpose ','autocomplete':'off'}),)

    email = forms.EmailField(max_length=254, validators=[alphanumeric],help_text='Required. Inform a valid email address.',required=True,widget=forms.TextInput(attrs= {'placeholder':'Enter Correct Email','autocomplete':'off'}))

    class Meta:
        model = User
        fields = ('username', 'name' ,'phone_number', 'gender', 'place', 'branch', 'cgpa_Btech', 'class_10_percentage', 'class_12_percentage', 'certifications_count', 'languages', 'sop','dob' , 'email','password1', 'password2', )
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(Student_SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['placeholder'] = "Enter username"


class UsdForm(forms.Form):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name = forms.CharField(max_length=30,validators=[alphanumeric], required=True, help_text='*required')
    email = forms.EmailField(max_length=254,validators=[alphanumeric], help_text='Required. Inform a valid email address.', required=True)
    place = forms.CharField(max_length=30,validators=[alphanumeric], required=True)
    cgpa_Btech = forms.FloatField(max_value=10, min_value=1, required=True,help_text='*required')
    class_10_percentage = forms.FloatField(max_value=100, min_value=0, required=True,help_text='*required')
    class_12_percentage = forms.FloatField(max_value=100, min_value=0, required=True, help_text='*required')
    certifications_count = forms.IntegerField(required=True)
    languages = forms.CharField(max_length=100, required=True, help_text='*required')

    sop = forms.CharField(max_length=500, validators=[alphanumeric],required=True)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{10,10}$',required=True)


class dispstuForm(forms.ModelForm):
    class Meta:
        model=stu_details
        fields=('username','phone_number','place','branch','cgpa_Btech','class_10_percentage',  'class_12_percentage','certifications_count',
               'languages','sop','dob')


c_type = (
    ('product', 'product'),
    ('service', 'service'))


class company_SignUpForm(UserCreationForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    company_name = forms.CharField(max_length=30, required=True,validators=[alphanumeric], help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Enter Company Name','autocomplete':'off'}))
    est_year=forms.IntegerField(required=True,help_text="*required",widget=forms.TextInput(attrs= {'placeholder':'Enter Est Year','autocomplete':'off'}))
    hr_name=forms.CharField(max_length=30, required=True, help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Enter HR Name','autocomplete':'off'}))
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{10,10}$")
    hr_phn = forms.RegexField(regex=r'^\+?1?\d{10,10}$',widget=forms.TextInput(attrs= {'placeholder':'Enter Phone Number','autocomplete':'off'}))
    headquaters=forms.CharField(max_length=30, validators=[alphanumeric],required=True, help_text='*required',widget=forms.TextInput(attrs= {'placeholder':'Enter Headquarter Location','autocomplete':'off'}))
    about=forms.CharField(max_length=1000,validators=[alphanumeric], required=True, help_text='*required',widget=forms.Textarea(attrs= {'placeholder':'Write About Your Company','autocomplete':'off'}))
    type=forms.ChoiceField(required=True,choices=c_type)
    email = forms.EmailField(max_length=254,validators=[alphanumeric], help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs= {'placeholder':'Enter Correct Email','autocomplete':'off'}))
    class Meta:
        model = User
        fields = ('username', 'company_name', 'est_year','hr_name','hr_phn','headquaters','about','type','email','password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(company_SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['placeholder'] = "Enter Company Username"


class ccdForm(forms.Form):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    hr_name = forms.CharField(max_length=30, required=True,validators=[alphanumeric], help_text='*required')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{10,10}$")
    hr_phn = forms.RegexField(regex=r'^\+?1?\d{10,10}$')
    about=forms.CharField(max_length=1000, required=True,validators=[alphanumeric], help_text='*required')






class jobposFormm(forms.ModelForm):
    class Meta:
        model=job_poss
        fields=('company_name','username','job_id','designation' , 'roless', 'salary'  ,'bond_years', 'perkss', 'information_technology','mech', 'civil','eee',  'ece', 'chemical' ,'cse')


