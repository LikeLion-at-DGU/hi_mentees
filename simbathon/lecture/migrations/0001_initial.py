# Generated by Django 3.2.3 on 2021-06-20 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('level', models.CharField(choices=[('star1', '1단계'), ('star2', '2단계'), ('star3', '3단계'), ('star4', '4단계'), ('star5', '5단계')], max_length=10)),
                ('app_start_date', models.DateField()),
                ('app_end_date', models.DateField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('schedule', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lecture.category')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
