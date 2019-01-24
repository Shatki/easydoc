# Generated by Django 2.1.5 on 2019-01-22 18:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counterparties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterpart',
            name='employees',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='сотрудники'),
        ),
    ]
