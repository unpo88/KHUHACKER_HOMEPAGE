# Generated by Django 3.0.4 on 2020-03-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.CharField(choices=[('남', '남자'), ('여', '여자')], max_length=10, verbose_name='성별'),
        ),
    ]
