# Generated by Django 3.2.13 on 2022-05-15 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_auto_20220514_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='specific_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]