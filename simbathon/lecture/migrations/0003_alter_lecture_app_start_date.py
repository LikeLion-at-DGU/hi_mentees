# Generated by Django 3.2.3 on 2021-06-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_alter_lecture_app_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='app_start_date',
            field=models.DateTimeField(),
        ),
    ]
