# Generated by Django 3.0.4 on 2020-03-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('sex', models.CharField(choices=[('남', '남자'), ('여', '여자')], max_length=1, verbose_name='성별')),
                ('birthday', models.DateField(verbose_name='생년월일')),
                ('student_id', models.CharField(max_length=15, verbose_name='학번')),
                ('major', models.CharField(choices=[('컴공', '컴퓨터공학과'), ('전자', '전자공학과')], max_length=30, verbose_name='전공')),
                ('hacker', models.CharField(max_length=15, verbose_name='기수')),
                ('phone', models.CharField(max_length=30, verbose_name='연락처')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
