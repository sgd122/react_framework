# Generated by Django 2.2.7 on 2019-11-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20191130_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='sort',
            field=models.IntegerField(null=True, verbose_name='sort'),
        ),
    ]
