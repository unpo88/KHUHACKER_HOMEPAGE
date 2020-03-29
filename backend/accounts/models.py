from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, sex, birthday, student_id, major, hacker, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            sex=sex,
            birthday=birthday,
            student_id=student_id,
            major=major,
            hacker=hacker,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, sex, birthday, student_id, major, hacker, phone, password=None):
        user = self.create_user(
            email,
            password=password,
            sex=sex,
            birthday=birthday,
            student_id=student_id,
            major=major,
            hacker=hacker,
            phone=phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )

    name = models.CharField(verbose_name='이름', max_length=30)
    
    SEX_CHOICES = [
        ('남', '남자'),
        ('여', '여자'),
    ]
    sex = models.CharField(verbose_name='성별', max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(verbose_name='생년월일')
    student_id = models.CharField(verbose_name='학번', max_length=15)

    MAJOR_CHOICES = [
        ('컴공', '컴퓨터공학과'),
        ('전자', '전자공학과'),
    ]

    major = models.CharField(verbose_name='전공', max_length=30, choices=MAJOR_CHOICES)
    hacker = models.CharField(verbose_name='기수', max_length=15)
    phone = models.CharField(verbose_name='연락처', max_length=30)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'sex', 'birthday', 'student_id', 'major', 'hacker', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
