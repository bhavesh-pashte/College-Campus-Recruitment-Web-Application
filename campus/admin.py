from django.contrib import admin
from campus.models import stu_details,comp_details,applied_jobs,job_poss, Exam, Exam_1, Exam_2, Exam_3
from django.contrib.auth.admin import UserAdmin
admin.site.register(stu_details)
admin.site.register(comp_details)
admin.site.register(job_poss)
admin.site.register(applied_jobs)
admin.site.register(Exam)
admin.site.register(Exam_1)
admin.site.register(Exam_2)
admin.site.register(Exam_3)
