from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
done = (
    ('yes', 'yes'),
    ('no', 'no'),
)


class stu_details(models.Model):
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
        ('others','others'))
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    username=models.CharField(max_length=9, blank=False,help_text="enter username ex:y16it***",default="y1")
    name = models.CharField(max_length=30, blank=False,validators=[alphanumeric], help_text='*required', default="full name")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,10}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 10)
    gender=models.CharField(blank=False, choices=gender,max_length=10)
    place = models.CharField(max_length=30,validators=[alphanumeric], blank=False)
    branch = models.CharField(blank=False, choices=branch_choices, max_length=10)
    cgpa_Btech = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
    class_10_percentage = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='*required')
    class_12_percentage = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='*required')
    certifications_count = models.IntegerField(blank=False)
    languages = models.CharField(max_length=100, blank=False, help_text='*required')
    sop = models.CharField(max_length=500, validators=[alphanumeric],default="statement of purpose", help_text='*required')
    dob = models.DateField(blank=False, help_text='*format is YYYY-MM-DD', )
    email = models.EmailField(max_length=254, blank=False, help_text='Required. Inform a valid email address.',default="anudeep.insvirat@gmail.com")

    def __str__(self):
        return self.username


class comp_details(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    username=models.CharField(max_length=30,blank=False , help_text='*required')
    company_name = models.CharField(validators=[alphanumeric],max_length=30, blank=False, help_text='*required')
    est_year = models.IntegerField( blank=False, help_text="*required")
    hr_name = models.CharField(max_length=30,validators=[alphanumeric], blank=False, help_text='*required')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,10}$")
    hr_phn = models.CharField(validators = [phoneNumberRegex], max_length = 10)
    headquaters = models.CharField(max_length=30,validators=[alphanumeric],blank=False, help_text='*required')
    about = models.CharField(max_length=1000, validators=[alphanumeric],blank=False, help_text='*required')
    type = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254,validators=[alphanumeric],blank=False, help_text='Required. Inform a valid email address.')

    def __str__(self):
        return self.username


class job_poss(models.Model):
    job_id=models.CharField(max_length=30, blank=False, help_text='*required',unique=True)
    username = models.CharField(max_length=30, blank=False, help_text='*required')
    company_name = models.CharField(max_length=30, blank=False, help_text='*required')
    designation = models.CharField(max_length=30, blank=False, help_text='*required')
    roless=models.CharField(max_length=200,blank=False,help_text='*required')
    salary=models.IntegerField( blank=False, help_text='*required')
    bond_years=models.IntegerField( blank=False, help_text='*required')
    perkss = models.CharField(max_length=200, blank=False, help_text='*required')
    information_technology= models.CharField(blank=False, choices=done, max_length=10)
    mech= models.CharField(blank=False, choices=done, max_length=10)
    civil= models.CharField(blank=False, choices=done, max_length=10)
    eee = models.CharField(blank=False, choices=done, max_length=10)
    ece= models.CharField(blank=False, choices=done, max_length=10)
    chemical= models.CharField(blank=False, choices=done, max_length=10)
    cse= models.CharField(blank=False, choices=done, max_length=10)

    def __str__(self):
        return self.job_id


class applied_jobs(models.Model):
    company_id = models.CharField(max_length=30, blank=False, help_text='*required' ,default="company id")
    job_id = models.CharField(max_length=30, blank=False, help_text='*required',default="job id")
    student_id= models.CharField(max_length=9, blank=False, help_text="enter username ex:y16it***", default="y1")

    def __str__(self):
        return self.job_id



class Exam(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)


class Exam_1(models.Model):
    Question1 = models.CharField(max_length=100)
    Option11 = models.CharField(max_length=100)
    Option22 = models.CharField(max_length=100)
    Option33 = models.CharField(max_length=100)
    Option44 = models.CharField(max_length=100)
    Corrans1 = models.CharField(max_length=100)


class Exam_2(models.Model):
    Question2 = models.CharField(max_length=100)
    Option111 = models.CharField(max_length=100)
    Option222 = models.CharField(max_length=100)
    Option333 = models.CharField(max_length=100)
    Option444 = models.CharField(max_length=100)
    Corrans2 = models.CharField(max_length=100)


class Exam_3(models.Model):
    Question3 = models.CharField(max_length=100)
    Option1111 = models.CharField(max_length=100)
    Option2222 = models.CharField(max_length=100)
    Option3333 = models.CharField(max_length=100)
    Option4444 = models.CharField(max_length=100)
    Corrans3 = models.CharField(max_length=100)
