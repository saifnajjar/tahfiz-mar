# Generated by Django 4.2.4 on 2023-09-28 07:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الحلقة')),
                ('masjed_name', models.CharField(max_length=100, verbose_name='اسم المسجد')),
                ('address', models.TextField(verbose_name='عنوان المسجد')),
                ('work_schedule', models.CharField(max_length=255, verbose_name='وقت تفعيل الحلقة')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students/', verbose_name='صورة الطالب')),
                ('full_name', models.CharField(max_length=100, verbose_name='الإسم رباعي')),
                ('id_number', models.CharField(max_length=14, unique=True, verbose_name='رقم الهوية')),
                ('birth_date', models.DateField(verbose_name='تاريخ الميلاد')),
                ('address', models.TextField(verbose_name='عنوان السكن')),
                ('personal_mobile', models.CharField(blank=True, max_length=15, null=True, verbose_name='رقم الجوال الشخصي (اختياري)')),
                ('guardian_mobile', models.CharField(max_length=15, verbose_name='رقم جوال ولي الأمر')),
                ('current_hifz', models.CharField(max_length=100, verbose_name='الحفظ الحالي')),
                ('education_stage', models.CharField(max_length=100, verbose_name='المستوى الدراسي')),
                ('Monthly_absence', models.PositiveIntegerField(default=0, verbose_name='عدد أيام الغياب')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_count', models.PositiveIntegerField(verbose_name='عدد الأجزاء')),
                ('initial_part_number', models.PositiveIntegerField(verbose_name='من بداية جزء')),
                ('final_part_number', models.PositiveIntegerField(verbose_name='إلى نهاية جزء')),
                ('test_date', models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الإختبار')),
                ('result', models.IntegerField(verbose_name='معدل الإختبار')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='الإسم رباعي')),
                ('image', models.ImageField(upload_to='teachers/', verbose_name='صورة المحفظ')),
                ('id_number', models.CharField(max_length=14, unique=True, verbose_name='رقم الهوية')),
                ('date_of_birth', models.DateField(verbose_name='تاريخ الميلاد')),
                ('address', models.TextField(verbose_name='عنوان السكن')),
                ('personal_mobile', models.CharField(max_length=15, verbose_name='رقم الجوال')),
                ('Monthly_absence', models.PositiveIntegerField(default=0, verbose_name='عدد أيام الغياب')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='mohaffiz.circle')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='mohaffiz.teacher', verbose_name='اختر المحفظ'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان الشهادة')),
                ('description', models.TextField(verbose_name='وصف الشهادة')),
                ('image', models.ImageField(upload_to='certificates/', verbose_name='صورة الشهادة')),
                ('issue_date', models.DateField(verbose_name='تاريخ الحصول على الشهادة')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='mohaffiz.teacher', verbose_name='المحفظ')),
            ],
        ),
    ]
