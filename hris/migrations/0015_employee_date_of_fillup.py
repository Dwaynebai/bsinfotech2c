# Generated by Django 5.0.4 on 2024-05-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0014_rename_coll_bdc_employee_college_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='DATE_OF_FILLUP',
            field=models.DateField(blank=True, null=True),
        ),
    ]
