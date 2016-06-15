from django.contrib import admin
import models

class DoctorAdmin(admin.ModelAdmin):
    """docstring for DoctorAdmin"""
    list_display = ('user', 'sex', 'age', 'dept', 'post', 'title', 'phone', 'address', 'hospital')
    list_filter = ('sex','dept','hospital')
    search_fields = ('user',)
    ordering = ('-user',)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'add', 'ps', 'diagnose', 'sex', 'birthday')
    list_filter = ('sex', 'occupation')
    search_fields = ('user',)
    ordering = ('user',)

admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Patient, PatientAdmin)
