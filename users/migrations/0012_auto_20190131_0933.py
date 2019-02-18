# Generated by Django 2.1.5 on 2019-01-31 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190129_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pseudonym',
            field=models.CharField(db_index=True, max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$', message='допустимы только буквенные символы.')], verbose_name='псевдоним пользователя в системе'),
        ),
    ]
