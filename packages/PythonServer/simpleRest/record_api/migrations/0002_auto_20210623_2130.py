# Generated by Django 3.2.4 on 2021-06-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_records',
            name='illness',
        ),
        migrations.RemoveField(
            model_name='new_records',
            name='year',
        ),
        migrations.AddField(
            model_name='new_records',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='new_records',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
