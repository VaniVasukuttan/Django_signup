# Generated by Django 3.0 on 2020-01-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_facultyleave_studentleave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyleave',
            name='l_status',
            field=models.CharField(default='Pending', max_length=500),
        ),
        migrations.AlterField(
            model_name='studentleave',
            name='l_status',
            field=models.CharField(default='Pending', max_length=500),
        ),
    ]
