# Generated by Django 2.1.5 on 2019-01-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_counterpart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='counterpart',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_company',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
