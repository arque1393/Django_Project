# Generated by Django 4.1.2 on 2022-10-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others`')], max_length=30),
        ),
    ]