# Generated by Django 3.0.7 on 2020-06-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0003_auto_20200627_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fechaRealizacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
