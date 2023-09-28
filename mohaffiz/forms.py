from django import forms
from .models import Circle, Teacher, Student, Test

class CircleForm(forms.ModelForm):
    class Meta:
        model = Circle
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'masjed_name': forms.TextInput(attrs={'class': 'form-control'}),
            'work_schedule': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            


        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'Monthly_absence': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'circle': forms.Select(attrs={'class': 'form-control'}),

        }
        

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'personal_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'current_hifz': forms.TextInput(attrs={'class': 'form-control'}),
            'education_stage': forms.TextInput(attrs={'class': 'form-control'}),
            'Monthly_absence': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
        }
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        



from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'


    issue_date = forms.DateField(
        label='تاريخ الحصول على الشهادة',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )    
# class AchievementForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = '__all__'



# class RecitationForm(forms.ModelForm):
#     class Meta:
#         model = Recitation
#         fields = '__all__'
