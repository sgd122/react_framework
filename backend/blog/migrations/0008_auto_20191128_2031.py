# Generated by Django 2.2.7 on 2019-11-28 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191128_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='createDate',
        ),
    ]
