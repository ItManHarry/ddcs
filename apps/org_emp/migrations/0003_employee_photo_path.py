# Generated by Django 4.2.1 on 2023-06-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_emp', '0002_employee_email_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo_path',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
