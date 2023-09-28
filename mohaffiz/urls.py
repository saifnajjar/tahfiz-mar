from django.urls import path
from . import views

urlpatterns = [
    # مسارات الصفحات الرئيسية
    path('', views.dashboard, name='dashboard'),
    path('circles/', views.circle_list, name='circle_list'),
    path('circles/<int:circle_id>/', views.circle_detail, name='circle_detail'),
    path('circle_update/<int:id>', views.circle_update, name='circle_update'),
    path('circle_delete/<int:id>', views.circle_delete, name='circle_delete'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher_update/<int:id>', views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:id>', views.teacher_delete, name='teacher_delete'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('tests/', views.test_list, name='test_list'),
    path('tests/<int:test_id>/', views.test_detail, name='test_detail'),
    # path('achievements/', views.achievement_list, name='achievement_list'),
    # path('achievements/<int:achievement_id>/', views.achievement_detail, name='achievement_detail'),
    # path('recitations/', views.recitation_list, name='recitation_list'),
    # path('recitations/<int:recitation_id>/', views.recitation_detail, name='recitation_detail'),
    # path('honor_roll/', views.honor_roll, name='honor_roll'),


    # مسارات إضافة سجلات جديدة
    path('create_circle/', views.create_circle, name='create_circle'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_test/', views.create_test, name='create_test'),
    path('teacher/<int:teacher_id>/', views.teacher_profile, name='teacher_profile'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('confirm_student_delete/<int:student_id>/', views.confirm_student_delete, name='confirm_student_delete'),
    path('student_profile/<int:student_id>/', views.student_profile, name='student_profile'),
    path('create_certificate/', views.create_certificate, name='create_certificate'),


    # path('create_achievement/', views.create_achievement, name='create_achievement'),
    # path('create_recitation/', views.create_recitation, name='create_recitation'),
    
]
