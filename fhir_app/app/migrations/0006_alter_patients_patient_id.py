# Generated by Django 4.2.1 on 2023-05-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_patients_patient_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patients",
            name="patient_id",
            field=models.CharField(default=None, unique=True),
        ),
    ]
