from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Count
from .models import Circle, Teacher, Student, Test
from .forms import CircleForm, TeacherForm, StudentForm, TestForm
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date
from django.conf import settings
from django.db.models import Q

# Create your views here.
# def home_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request,'index.html')


def dashboard(request):
    circle_count = Circle.objects.all().count()
    teacher_count = Teacher.objects.all().count()
    student_count = Student.objects.all().count()
    test_count = Test.objects.all().count()
    context = {
        "circle_count": circle_count,
        "teacher_count": teacher_count,
        "student_count": student_count,
        "test_count": test_count,
    }
    return render(request, "dashboard.html", context)


def circle_list(request):
    circles = Circle.objects.all()
    return render(request, "circle_list.html", {"circles": circles})


def circle_detail(request, circle_id):
    circle = get_object_or_404(Circle, pk=circle_id)
    return render(request, "circle_detail.html", {"circle": circle})

def create_circle(request):
    if request.method == "POST":
        form = CircleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("circle_list")
    else:
        form = CircleForm()

    return render(request, "create_circle.html", {"form": form})


def circle_update(request, id):
    circle_id = Circle.objects.get(id=id)
    if request.method == "POST":
        circle_save = CircleForm(request.POST, instance=circle_id)
        if circle_save.is_valid():
            circle_save.save()
            return redirect("circle_list")
    else:
        circle_save = CircleForm(instance=circle_id)
    context = {
        "form": circle_save,
    }

    return render(request, "circle_update.html", context)


def circle_delete(request, id):
    circle_delete = get_object_or_404(Circle, id=id)
    if request.method == "POST":
        circle_delete.delete()
        return redirect("circle_list")

    return render(request, "circle_delete.html")


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    certificates = (
        teacher.certificates.all()
    )  # الحصول على جميع الشهادات المرتبطة بالمحفظ
    return render(
        request,
        "teacher_detail.html",
        {"teacher": teacher, "certificates": certificates},
    )

def teacher_update(request, id):
    teacher_id = Teacher.objects.get(id=id)
    if request.method == "POST":
        teacher_save = TeacherForm(request.POST, request.FILES, instance=teacher_id)
        if teacher_save.is_valid():
            teacher_save.save()
            return redirect("teacher_list")
    else:
        teacher_save = TeacherForm(instance=teacher_id)
    context = {
        "form": teacher_save,
    }

    return render(request, "teacher_update.html", context)


def teacher_delete(request, id):
    teacher_delete = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        teacher_delete.delete()
        return redirect("teacher_list")

    return render(request, "teacher_delete.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "student_detail.html", {"student": student})


def test_list(request):
    tests = Test.objects.all()
    return render(request, "test_list.html", {"tests": tests})


def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return render(request, "test_detail.html", {"test": test})







def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    else:
        form = TeacherForm()

    return render(request, "create_teacher.html", {"form": form})


def create_student(request):
    teachers = Teacher.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)  # قم بتمرير request.FILES للتعامل مع ملف الصورة
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "create_student.html", {"form": form, "teachers": teachers})


def create_test(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("test_list")
    else:
        form = TestForm()

    return render(request, "create_test.html", {"form": form})



from django.shortcuts import render, get_object_or_404
from .models import Teacher

def teacher_profile(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    students = teacher.students.all()  # استعلام لجلب الطلاب الخاصين بالمحفظ

    return render(request, 'teacher_profile.html', {'teacher': teacher, 'students': students})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form, 'student': student})



def confirm_student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  # توجيه المستخدم بعد الحذف

    return render(request, 'confirm_student_delete.html', {'student': student})




def student_profile(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    return render(request, 'student_profile.html', {'student': student})





from django.shortcuts import render, redirect
from .models import Certificate
from .forms import CertificateForm

def create_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # توجيه المستخدم إلى صفحة قائمة المحفظين بعد الحفظ
    else:
        form = CertificateForm()
    
    return render(request, 'create_certificate.html', {'form': form})

# def create_achievement(request):
#     if request.method == 'POST':
#         form = AchievementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('achievement_list')
#     else:
#         form = AchievementForm()

#     return render(request, 'create_achievement.html', {'form': form})


# def create_recitation(request):
#     if request.method == 'POST':
#         form = RecitationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('recitation_list')
#     else:
#         form = RecitationForm()

#     return render(request, 'create_recitation.html', {'form': form})

# def honor_roll(request):
#     top_students = Student.objects.order_by('-Monthly_absence')[:10]
#     top_teachers = Teacher.objects.order_by('-Monthly_absence')[:10]
#     top_circles = Circle.objects.annotate(student_count=Count('student')).order_by('-student_count')[:10]

#     return render(request, 'honor_roll.html', {
#         'top_students': top_students,
#         'top_teachers': top_teachers,
#         'top_circles': top_circles,
#     })
