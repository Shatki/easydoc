# Generated by Django 2.1.5 on 2019-01-22 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190122_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nickname',
            new_name='name',
        ),
    ]
