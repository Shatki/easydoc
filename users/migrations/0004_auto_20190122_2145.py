# Generated by Django 2.1.5 on 2019-01-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190122_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='defaultprofileimage.jpg', null=True, upload_to='', verbose_name='аватар'),
        ),
    ]
