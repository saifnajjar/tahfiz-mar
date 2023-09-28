from django.contrib import admin
from .models import Circle, Teacher, Student, Test, Certificate 

class CircleAdmin(admin.ModelAdmin):
    list_display = ['name', 'masjed_name', 'address', 'work_schedule']
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'personal_mobile', 'id_number', 'Monthly_absence']
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'id_number', 'teacher', 'Monthly_absence']
    
class TestAdmin(admin.ModelAdmin):
    list_display = ['student', 'test_date', 'result','parts_count','initial_part_number','final_part_number']

class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'issue_date', 'teacher', 'type']
    
    
# class AchievementAdmin(admin.ModelAdmin):
#     list_display = ['certificate_name', 'certificate_type', 'teacher']
    
    
# class RecitationAdmin(admin.ModelAdmin):
#     list_display = ['student', 'surah', 'recitation_date']
    
# class HonorRollAdmin(admin.ModelAdmin):
#     list_display = ['student', 'circle', 'teacher', 'achievement_type']

admin.site.register(Circle, CircleAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Certificate, CertificateAdmin)

# admin.site.register(Achievement, AchievementAdmin)
# admin.site.register(Recitation, RecitationAdmin)
# admin.site.register(HonorRoll, HonorRollAdmin)

# from .models import Doctor,Patient,Appointment,PatientDischargeDetails
# # Register your models here.
# class DoctorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Doctor, DoctorAdmin)

# class PatientAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Patient, PatientAdmin)

# class AppointmentAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Appointment, AppointmentAdmin)

# class PatientDischargeDetailsAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
