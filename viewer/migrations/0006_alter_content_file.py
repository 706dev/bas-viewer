# Generated by Django 3.2.13 on 2022-05-15 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_alter_content_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(upload_to='content/'),
        ),
    ]